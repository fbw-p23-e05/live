-- Left outer join (without OUTER clause)
SELECT * 
FROM basket_a
LEFT JOIN basket_b
	ON fruit_a = fruit_b
WHERE b_id IS NULL;

-- OR

-- Left outer join (with OUTER clause)
SELECT *
FROM basket_a
LEFT OUTER JOIN basket_b
	ON fruit_a = fruit_b
WHERE b_id IS NULL;