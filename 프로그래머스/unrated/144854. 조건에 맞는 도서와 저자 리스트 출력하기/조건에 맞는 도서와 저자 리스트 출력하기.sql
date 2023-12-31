SELECT B.BOOK_ID, A.AUTHOR_NAME, DATE_FORMAT(B.PUBLISHED_DATE, '%Y-%m-%d') AS PUBLISHED_DATE
FROM BOOK AS B
    LEFT JOIN AUTHOR AS A ON B.author_id = A.author_id
WHERE category LIKE "경제"
ORDER BY B.published_date