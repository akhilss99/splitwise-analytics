-- analyses/my_analysis.sql

-- Import the macro from the dbt_utils package

-- Use the macro
SELECT
    {{ generate_purchase_types('description', var('purchase_types')) }} AS status_label
FROM
    my_table
