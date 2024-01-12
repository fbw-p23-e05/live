-- Left Join
SELECT *
FROM basket_b
LEFT JOIN basket_a
	ON fruit_b = fruit_a;