
CREATE TEMPORARY TABLE runner_orders_post AS
	SELECT
		order_id,
		runner_id,
		pick_up_time,
		CAST(distance_km AS DECIMAL(3,1)) AS distance_km, 
		CAST(duration_mins AS INT) AS duration_mins,
		cancellation
    FROM runner_orders_pre;


