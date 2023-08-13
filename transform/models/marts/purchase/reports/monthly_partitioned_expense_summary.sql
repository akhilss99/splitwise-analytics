{% set column_names = dbt_utils.get_filtered_columns_in_relation(from=ref('monthly_partitioned_expense'), except=["month", "year"]) %}

with monthly_partitioned_expense_summary as (
    select 
        month,
        year,
        {% for column_name in column_names %}
            coalesce({{ column_name }}, 0) as {{ column_name }},
        {% endfor %}
    from
        {{ ref('monthly_partitioned_expense') }}
),

final as (
    select
        month,
        year,
        {% for column_name in column_names %}
            {{ column_name }},
        {% endfor %}
        {{ column_names | join(' + ') }} as total
    from
        monthly_partitioned_expense_summary
)

select * from final
