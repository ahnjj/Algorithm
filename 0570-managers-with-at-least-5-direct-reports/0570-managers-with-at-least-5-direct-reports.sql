SELECT b.name
FROM Employee AS a
     LEFT JOIN Employee AS b ON a.managerId = b.id
GROUP BY b.id
HAVING COUNT(b.id) >= 5