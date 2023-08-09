SELECT PRODUCT_CODE, SUM(P.price*O.sales_amount) AS 'SALES'
FROM product AS P
     LEFT JOIN offline_sale AS O ON P.product_id = O.product_id
GROUP BY P.product_code
ORDER BY SUM(P.price*O.sales_amount) DESC, P.product_code