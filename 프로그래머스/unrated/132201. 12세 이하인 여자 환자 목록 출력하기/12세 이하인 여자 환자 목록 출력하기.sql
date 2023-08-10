SELECT PT_NAME, PT_NO, GEND_CD, AGE
      , CASE  
            WHEN TLNO IS NULL THEN 'NONE' -- NULL 일때 표현하고 싶으면, CASE WHEN column IS NULL THEN --- 이렇게 쓸것!
            ELSE TLNO
        END AS TLNO
FROM patient
WHERE age <= 12 AND gend_cd = 'W'
ORDER BY age DESC, pt_name