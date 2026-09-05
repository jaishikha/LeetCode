# Write your MySQL query statement below
SELECT t.id
FROM Weather y
JOIN Weather t
WHERE DATEDIFF(t.recordDate, y.recordDate) = 1 AND t.temperature >  y.temperature;