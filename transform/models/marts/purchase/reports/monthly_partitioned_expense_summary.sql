with purchase_summary as (
    PIVOT 
        {{ ref('monthly_partitioned_expense') }} on purchase
    using sum(total_spent)
),

monthly_partitioned_expense_summary as (
    select 
        month,
        year,
        bigbasket,
        supermarket,
        swiggy,
        (bigbasket + instamart + supermarket + swiggy) as total
    from
        purchase_summary
)

select * from monthly_partitioned_expense_summary