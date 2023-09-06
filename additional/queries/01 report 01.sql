CREATE OR REPLACE FUNCTION "public"."get_report_01"("start_date" date, "end_date" date)
  RETURNS TABLE("etrap_id" int4, "etrap_name_0" varchar, "etrap_name_1" varchar, "etrap_name_2" varchar,
	"surgery_count" int4, "surgery_sum" numeric, "therapy_count" int4, "therapy_sum" numeric,
	"diagnosis_count" int4, "diagnosis_sum" numeric, "total_count" int4, "total_sum" numeric) AS $BODY$

BEGIN

	RETURN QUERY(

			SELECT etrap.id AS etrap_id, etrap.name_0 AS etrap_name_0, etrap.name_1 AS etrap_name_1, etrap.name_2 AS etrap_name_2,
			COALESCE(surgery.surgery_count, 0)::int4, COALESCE(surgery.surgery_sum, 0.0)::numeric,
			COALESCE(therapy.therapy_count, 0)::int4, COALESCE(therapy.therapy_sum, 0.0)::numeric,
			COALESCE(diagnosis.diagnosis_count, 0)::int4, COALESCE(diagnosis.diagnosis_sum, 0.0)::numeric,
			COALESCE(surgery.surgery_count, 0)::int4 + COALESCE(therapy.therapy_count, 0)::int4 + COALESCE(diagnosis.diagnosis_count, 0)::int4 AS total_count,
			COALESCE(surgery.surgery_sum, 0)::numeric + COALESCE(therapy.therapy_sum, 0)::numeric + COALESCE(diagnosis.diagnosis_sum, 0)::numeric AS total_sum

			FROM
					etrap
			LEFT JOIN
					(SELECT
							hospital.etrap_id AS etrap_id,
							COUNT(ps.id) AS surgery_count,
							SUM(ps.price_man) AS surgery_sum
					FROM patient_surgery AS ps
					INNER JOIN hospital ON ps.hospital_surgery_id = hospital.id
					WHERE ps.surgery_date BETWEEN start_date AND end_date
					GROUP BY hospital.etrap_id) surgery
			ON etrap.id = surgery.etrap_id

			LEFT JOIN

					(SELECT
							hospital.etrap_id AS etrap_id,
							COUNT(ts.id) AS therapy_count,
							SUM(ts.price_man) AS therapy_sum
					FROM patient_therapy AS ts
					INNER JOIN hospital ON ts.hospital_therapy_id = hospital.id
					WHERE ts.exit_date BETWEEN start_date AND end_date
					GROUP BY hospital.etrap_id) therapy
			ON etrap.id = therapy.etrap_id

			LEFT JOIN

					(SELECT
							hospital.etrap_id AS etrap_id,
							COUNT(ds.id) AS diagnosis_count,
							SUM(ds.price_man) AS diagnosis_sum
					FROM patient_diagnosis AS ds
					INNER JOIN hospital ON ds.hospital_id = hospital.id
					WHERE ds.exit_date BETWEEN start_date AND end_date
					GROUP BY hospital.etrap_id) diagnosis
			ON etrap.id = diagnosis.etrap_id

			ORDER BY etrap.name_2

	);


END$BODY$
  LANGUAGE plpgsql VOLATILE
  COST 100
  ROWS 1000;







etrap_id, etrap_name_0, etrap_name_1, etrap_name_2,
surgery_count, surgery_sum,
therapy_count, therapy_sum,
diagnosis_count, diagnosis_sum,
total_count, total_sum

'etrap_id', 'etrap_name_0', 'etrap_name_1', 'etrap_name_2',
'surgery_count', 'surgery_sum',
'therapy_count', 'therapy_sum',
'diagnosis_count', 'diagnosis_sum',
'total_count', 'total_sum',
