-- Full Outer Join
SELECT *
FROM basket_a 
FULL OUTER JOIN basket_b
	ON fruit_a = fruit_b
WHERE a_id IS NULL OR b_id IS NULL;