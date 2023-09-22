

with monthly_partitioned_expense_summary as (
    select 
        month,
        year,
        
    from
        "analyticsdb"."main_marts"."monthly_partitioned_expense"
),

final as (
    select
        month,
        year,
        
         as total
    from
        monthly_partitioned_expense_summary
)

select * from final