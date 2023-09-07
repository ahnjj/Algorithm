DELETE FROM Person
WHERE Id NOT IN (
SELECT sub.min_id
FROM(
  SELECT email, MIN(Id) AS min_id
FROM Person 
GROUP BY email
) sub )