SELECT Today.id
FROM Weather AS Yesterday
     INNER JOIN Weather AS Today ON DATE_ADD(yesterday.recordDate, INTERVAL 1 DAY) = Today.recordDate
WHERE Yesterday.temperature < Today.temperature

     