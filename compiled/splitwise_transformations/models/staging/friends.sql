with stg_friends as (
    select
        *
    from
        's3://splitwise-raw/friends/friends.parquet'
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