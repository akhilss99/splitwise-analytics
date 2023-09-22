with monthly_partitioned_expense as (
   select
      month,
      year,
      purchase_type,
      sum(cost) as total_spent
   from
      "analyticsdb"."main_intermediate"."purchases"
   where
      group_name in ('Flat 105')
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