/* Write your MySQL query statement below */
WITH Daily AS (
    SELECT 
        visited_on,
        SUM(amount) AS daily_amount
    FROM Customer
    GROUP BY visited_on
),
Sum7D AS (
    SELECT visited_on,
           SUM(daily_amount) OVER (ORDER BY visited_on ROWS BETWEEN 6 PRECEDING AND CURRENT ROW) AS amountSum, 
           MIN(visited_on) OVER() AS 1st_date
    FROM Daily
)

SELECT 
    visited_on,
    amountSum AS amount,
    ROUND(amountSum / 7, 2) AS average_amount
FROM Sum7D
WHERE visited_on >= 1st_date + 6;

