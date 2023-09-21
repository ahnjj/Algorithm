SELECT b.name
FROM Employee AS a,Employee AS b
WHERE a.managerId = b.id
GROUP BY b.id
HAVING COUNT(b.id) >= 5