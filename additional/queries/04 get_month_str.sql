CREATE OR REPLACE FUNCTION "public"."get_month_str"("p_date" date)
  RETURNS "pg_catalog"."varchar" AS $BODY$
BEGIN

	RETURN to_char(p_date, 'YYYY-MM');

END$BODY$
  LANGUAGE plpgsql VOLATILE
  COST 100