# Write your MySQL query statement below
WITH First_login AS (
    SELECT player_id, MIN(event_date) AS first_date
    FROM Activity
    GROUP BY player_id
)

SELECT ROUND(COUNT(CASE WHEN DATEDIFF(a.event_date, f.first_date) = 1 THEN 1 END) / COUNT(DISTINCT f.player_id), 2) AS fraction
FROM First_login f
JOIN Activity a
ON f.player_id = a.player_id;
