with stg_friends as (
    select
        *
    from
        {{ source('splitwise_source', 'friends') }}
),
renamed as (
    select
        id,
        first_name,
        last_name,
        email
    from
        stg_friends
)
select * from renamed