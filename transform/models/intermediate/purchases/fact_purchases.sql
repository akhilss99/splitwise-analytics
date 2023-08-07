with purchases as (
    select 
        month,
        year,
        group_name,
        description,
        cost,
        date,
        created_at,
        created_by,
        category,
        case 
            when 
                description not ilike '%instamart%' and
                description ilike '%swiggy%'
            then 'swiggy'
            when
                description ilike '%instamart%'
            then 'instamart'
            when
                description ilike '%supermarket%'
            then 'supermarket'
            when
                description ilike '%big%' and
                description ilike '%basket%'
            then 'bigbasket'
        end as purchase
    from
    {{ ref('fact_group_expenditures') }}
)

select * from purchases