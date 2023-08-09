with purchase_summary as (
    PIVOT 
        {{ ref('monthly_partitioned_expense') }} on purchase
    using sum(total_spent)
),

monthly_partitioned_expense_summary as (
    select 
        month,
        year,
        coalesce(bigbasket, 0) as bigbasket,
        coalesce(supermarket, 0) as supermarket,
        coalesce(swiggy, 0) as swiggy,
        coalesce(instamart, 0) as instamart
    from
        purchase_summary
),

final as (
    select
        *,
        bigbasket + instamart + supermarket + swiggy as total
    from
        monthly_partitioned_expense_summary
)

select * from final