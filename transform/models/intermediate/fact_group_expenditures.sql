with group_expenditures as (
    select
        g.id as group_id,
        g.name as group_name,
        e.description as description,
        e.payment as payment,
        e.cost as cost,
        e.date as date,
        e.year as year,
        e.month as month,
        e.created_at as created_at,
        e.created_by as created_by,
        e.category as category
    from
        {{ ref('stg_expense') }} e
        inner join {{ ref('stg_groups') }} g on e.group_id = g.id
        where e.active_ind = 1
)

select * from group_expenditures