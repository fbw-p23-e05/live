-- Implicit Join
SELECT fruit_a, fruit_b 
FROM basket_a, basket_b
WHERE basket_a.fruit_a = basket_b.fruit_b;