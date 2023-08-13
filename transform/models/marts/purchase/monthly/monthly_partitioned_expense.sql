with monthly_partitioned_expense as (
   select
      month,
      year,
      purchase_type,
      sum(cost) as total_spent
   from
      {{ ref('purchases') }}
   where
      group_name in ({% for group in var('groups') %}'{{ group }}'{% endfor %})
   group by
      month,
      year,
      purchase_type
),
purchase_summary as (
   PIVOT 
      monthly_partitioned_expense on purchase_type
   using sum(total_spent)
)

select * from purchase_summary