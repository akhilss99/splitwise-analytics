with stg_groups as (
    select
        *
    from
        's3://splitwise-raw/groups/groups.parquet'
),
renamed as (
    select
        id, 
        name,
        updated_at,
        created_at,
        group_type
    from 
        stg_groups
)

select * from renamed