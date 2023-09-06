CREATE OR REPLACE VIEW "public"."v_patient_event" AS SELECT
	patient_surgery.id AS original_id,
	'0-' || patient_surgery.id::text AS id,
	patient_surgery.created_at,
	0 AS event_type,
	patient_surgery.surgery_date AS event_date,
	surgery_type.name_0 || ': ' || substr(patient_surgery.diagnosis_0, 1, 50) AS description_0,
	surgery_type.name_1 || ': ' || substr(patient_surgery.diagnosis_1, 1, 50) AS description_1,
	surgery_type.name_2 || ': ' || substr(patient_surgery.diagnosis_2, 1, 50) AS description_2,
	COALESCE(patient_surgery.price_man, 0) AS price_man,
	patient_surgery.hospital_surgery_id AS hospital_id
FROM patient_surgery
LEFT JOIN surgery_type ON patient_surgery.surgery_type_id=surgery_type.id

UNION ALL

SELECT
	patient_therapy.id AS original_id,
	'1-' || patient_therapy.id::text AS id,
	patient_therapy.created_at,
	1 AS event_type,
	patient_therapy.exit_date AS event_date,
	substr(patient_therapy.diagnosis_0, 1, 50) AS description_0,
	substr(patient_therapy.diagnosis_1, 1, 50) AS description_1,
	substr(patient_therapy.diagnosis_2, 1, 50) AS description_2,
	COALESCE(patient_therapy.price_man, 0) AS price_man,
	patient_therapy.hospital_therapy_id AS hospital_id
FROM patient_therapy

UNION ALL

SELECT
	patient_diagnosis.id AS original_id,
	'2-' || patient_diagnosis.id::text AS id,
	patient_diagnosis.created_at,
	2 AS event_type,
	patient_diagnosis.exit_date AS event_date,
	substr(patient_diagnosis.diagnosis_0, 1, 50) AS description_0,
	substr(patient_diagnosis.diagnosis_1, 1, 50) AS description_1,
	substr(patient_diagnosis.diagnosis_2, 1, 50) AS description_2,
	COALESCE(patient_diagnosis.price_man, 0) AS price_man,
	patient_diagnosis.hospital_id
FROM patient_diagnosis

UNION ALL

SELECT
	patient_resolution.id AS original_id,
	'3-' || patient_resolution.id::text AS id,
	patient_resolution.created_at,
	3 AS event_type,
	patient_resolution.resolution_date AS event_date,
	patient_resolution.lastname_0 || ': ' || patient_resolution.resolution_name_0 AS description_0,
	patient_resolution.lastname_1 || ': ' || patient_resolution.resolution_name_1 AS description_1,
	patient_resolution.lastname_2 || ': ' || patient_resolution.resolution_name_2 AS description_2,
	0 AS price_man,
	-1 AS hospital_id
FROM patient_resolution;