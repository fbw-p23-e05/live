CREATE TABLE IF NOT EXISTS demo_stamp(
	ts_1 TIMESTAMP,
	ts_2 TIMESTAMPTZ
);

SET timezone = 'America/Los_Angeles';

INSERT INTO demo_stamp(
	ts_1,
	ts_2
)
VALUES ('2024-01-17 12:34:54', '2024-01-17 12:34:54');

SELECT * FROM demo_stamp;

