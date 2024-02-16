CREATE TEMPORARY TABLE cust_orders AS
  SELECT
	order_id,
	customer_id, 
	pizza_id, 
	CASE
	    WHEN exclusions = '' THEN NULL
		WHEN exclusions = 'null' THEN NULL
	ELSE exclusions
	END AS exclusions_cleaned,
	CASE
		WHEN extras = '' THEN null
		WHEN extras = 'NaN' THEN null
        WHEN extras = 'null' THEN NULL
	ELSE extras
	END AS extras_cleaned,
	order_time
  FROM customer_orders;