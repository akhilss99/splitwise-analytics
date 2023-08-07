with stg_groups as (
    select
        *
    from
        {{ source('splitwise_source', 'groups') }}
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