WITH source AS 
(
    SELECT
        date,
        symbol,
        action,
        quantity
    FROM
        {{ source('dbsales', 'movimentacao_commodities')}}
),

renamed as
(   
    SELECT
        cast(date as date) as date,
        symbol,
        action,
        quantity
    FROM
        source
)

SELECT
    *
FROM
    renamed