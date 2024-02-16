CREATE TEMPORARY TABLE runner_orders_pre AS
SELECT
	order_id,
	runner_id,
	CASE
		WHEN pickup_time = 'null' THEN null
		ELSE pickup_time
	END AS pick_up_time,
	CASE
		WHEN distance = 'null' THEN null
		ELSE regexp_replace(distance, '[a-z]+', '')
	END AS distance_km,
	CASE
		WHEN duration = 'null' THEN null
		ELSE regexp_replace(duration, '[a-z]+', '')
		END AS duration_mins,
	CASE
		WHEN cancellation = '' THEN null
		WHEN cancellation = 'null' THEN null
		ELSE cancellation
		END AS cancellation               
FROM runner_orders;