CREATE OR REPLACE FUNCTION "public"."get_report_02"("start_date" date, "end_date" date, "etrap" int4='-1'::integer)
  RETURNS TABLE("id" int8, "month_name" varchar, "surgery_count" int4, "surgery_sum" numeric, "therapy_count" int4, "therapy_sum" numeric, "diagnosis_count" int4, "diagnosis_sum" numeric, "total_count" int4, "total_sum" numeric) AS $BODY$

BEGIN

	RETURN QUERY(

			SELECT ROW_NUMBER() OVER() AS id, pevent.month_name,
			COALESCE(surgery.surgery_count, 0)::int4, COALESCE(surgery.surgery_sum, 0.0)::numeric,
			COALESCE(therapy.therapy_count, 0)::int4, COALESCE(therapy.therapy_sum, 0.0)::numeric,
			COALESCE(diagnosis.diagnosis_count, 0)::int4, COALESCE(diagnosis.diagnosis_sum, 0.0)::numeric,
			COALESCE(surgery.surgery_count, 0)::int4 + COALESCE(therapy.therapy_count, 0)::int4 + COALESCE(diagnosis.diagnosis_count, 0)::int4 AS total_count,
			COALESCE(surgery.surgery_sum, 0)::numeric + COALESCE(therapy.therapy_sum, 0)::numeric + COALESCE(diagnosis.diagnosis_sum, 0)::numeric AS total_sum

			FROM
					(SELECT DISTINCT get_month_str(event_date) AS month_name
					 FROM v_patient_event
					 WHERE (v_patient_event.event_type IN (0, 1, 2))
										AND (CASE WHEN etrap >= 0
										          THEN v_patient_event.hospital_id IN (SELECT hospital.id FROM hospital
																																	 WHERE hospital.etrap_id = etrap)
															ELSE True
												 END)
-- 									AND (v_patient_event.event_date IS NOT NULL)
									) pevent
			LEFT JOIN
					(SELECT
							get_month_str(ps.surgery_date) AS month_name,
							COUNT(ps.id) AS surgery_count,
							SUM(ps.price_man) AS surgery_sum
					FROM patient_surgery AS ps
					INNER JOIN hospital ON ps.hospital_surgery_id = hospital.id
					WHERE ps.surgery_date BETWEEN start_date AND end_date
					GROUP BY month_name) surgery
			ON pevent.month_name = surgery.month_name

			LEFT JOIN

					(SELECT
							get_month_str(ts.exit_date) AS month_name,
							COUNT(ts.id) AS therapy_count,
							SUM(ts.price_man) AS therapy_sum
					FROM patient_therapy AS ts
					INNER JOIN hospital ON ts.hospital_therapy_id = hospital.id
					WHERE ts.exit_date BETWEEN start_date AND end_date
					GROUP BY month_name) therapy
			ON pevent.month_name = therapy.month_name

			LEFT JOIN

					(SELECT
							get_month_str(ds.diagnosis_date) AS month_name,
							COUNT(ds.id) AS diagnosis_count,
							SUM(ds.price_man) AS diagnosis_sum
					FROM patient_diagnosis AS ds
					INNER JOIN hospital ON ds.hospital_id = hospital.id
					WHERE ds.exit_date BETWEEN start_date AND end_date
					GROUP BY month_name) diagnosis
			ON pevent.month_name = diagnosis.month_name
			ORDER BY pevent.month_name

		);


END$BODY$
  LANGUAGE plpgsql VOLATILE
  COST 100
  ROWS 1000