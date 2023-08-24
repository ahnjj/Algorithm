SELECT S.machine_id, ROUND(AVG(ABS(E.timestamp - S.timestamp)),3) AS processing_time
FROM Activity AS S
    LEFT JOIN Activity AS E ON S.machine_id = E.machine_id AND S.process_id = E.process_id AND S.activity_type != E.activity_type
GROUP BY S.machine_id
