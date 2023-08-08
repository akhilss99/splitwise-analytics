with stg_expense as (
    select
        *
    from
        {{ source('splitwise_source', 'expense') }}
),
renamed as (
    select
        id,
        group_id,
        description,
        payment,
        creation_method,
        transaction_method,
        transaction_confirmed,
        cost,
        currency_code,
        date,
        month,
        year,
        created_at,
        updated_at,
        deleted_at,
        transaction_id,
        created_by,
        category,
        updated_by,
        deleted_by,
        active_ind
    from
        stg_expense
)

select * from renamed