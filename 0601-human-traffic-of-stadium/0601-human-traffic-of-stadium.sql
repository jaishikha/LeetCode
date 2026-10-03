# Write your MySQL query statement below
WITH Evaluated AS (
    SELECT 
        id, 
        visit_date, 
        people,
        LAG(people, 1) OVER (ORDER BY id) AS prev1_people,
        LAG(people, 2) OVER (ORDER BY id) AS prev2_people,
        LEAD(people, 1) OVER (ORDER BY id) AS next1_people,
        LEAD(people, 2) OVER (ORDER BY id) AS next2_people
    FROM Stadium
)

SELECT DISTINCT id, visit_date, people
FROM Evaluated
WHERE 
    (people >= 100 AND next1_people >= 100 AND next2_people >= 100)
    OR (prev1_people >= 100 AND people >= 100 AND next1_people >= 100)
    OR (prev2_people >= 100 AND prev1_people >= 100 AND people >= 100)
ORDER BY visit_date ASC;
