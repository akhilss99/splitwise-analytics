with purchases as (
    select 
        month,
        year,
        group_name,
        description,
        cost,
        date,
        category,
        {{ generate_purchase_types('description', var('purchase_types')) }} as purchase_type
    from
        {{ ref('fact_group_expenditures') }}
    where 
        purchase_type is not null
)

select * from purchases