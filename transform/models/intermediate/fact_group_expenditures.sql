with group_expenditures as (
    select
        g.name as group_name,
        e.description as description,
        e.payment as payment,
        e.cost as cost,
        e.date as date,
        e.year as year,
        e.month as month,
        e.category as category
    from
        {{ ref('expense') }} e
        inner join {{ ref('groups') }} g on e.group_id = g.id
        where e.active_ind = 1
)

select * from group_expenditures