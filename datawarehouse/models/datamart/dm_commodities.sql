-- models/datamart/dm_commodities.sql

WITH commodities AS
(
    SELECT
        date,
        symbol,
        close_price
    FROM
        {{ ref('stg_commodities')}}
),

movimentacao AS
(   
    SELECT
        date,
        symbol,
        action,
        quantity
    FROM
        {{ ref('stg_movimentacao_commodities')}}
),

joined AS
(
    SELECT
        c.date,
        c.symbol,
        c.close_price,
        m.action,
        m.quantity,
        (m.quantity * c.close_price) as value,
        CASE
            WHEN m.action = 'sell' THEN (m.quantity * c.close_price)
            ELSE -(m.quantity * c.close_price)
        END AS profit
    FROM
        commodities c
    INNER JOIN
        movimentacao m
        ON 
            c.date = m.date 
            AND c.symbol = m.symbol
),

last_day AS
(
    SELECT
        max(date) AS max_date
    FROM
        joined
),

filtered AS
(
    SELECT
        *
    FROM
        joined
    WHERE
        date = (select max_date FROM last_day)
)

SELECT
    date,
    symbol,
    close_price,
    action,
    quantity,
    value,
    profit
FROM
    filtered


