-- import

with source as 
(   SELECT
        "Date",
        "Close",
        "simbol"
    FROM 
        {{ source ('dbsales', 'commodities') }}
),

-- renamed

renamed as
(   SELECT
        CAST("Date" as date) as date,
        "Close" as close_price,
        simbol as symbol
    FROM
        source

)

SELECT * FROM renamed