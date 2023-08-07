with monthly_partitioned_expense as (
   select
      month,
      year,
      purchase,
      sum(cost) as total_spent
   from
      {{ ref('fact_purchases') }}
   where
      group_name = 'Flat 105' 
   group by
      month,
      year,
      purchase
)

select * from monthly_partitioned_expense
