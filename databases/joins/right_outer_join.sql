-- Right outer join (without the OUTER clause)
SELECT * 
FROM basket_a
RIGHT JOIN basket_b
	ON fruit_a = fruit_b
WHERE a_id IS NULL;

-- Right outer join (with the OUTER clause)
SELECT *
FROM basket_a
RIGHT OUTER JOIN basket_b
	ON fruit_a = fruit_b
WHERE a_id IS NULL;