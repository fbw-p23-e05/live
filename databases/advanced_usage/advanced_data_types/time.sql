CREATE TABLE IF NOT EXISTS shifts (
	shift_id SERIAL PRIMARY KEY,
	shift_name VARCHAR NOT NULL,
	start_at TIME NOT NULL,
	end_at TIME NOT NULL
);

INSERT INTO shifts(
	shift_name,
	start_at,
	end_at
)
VALUES('Morning', '07:00:00', '12:00:00'),
		('Afternoon', '13:00:00', '17:00:00'),
		('Night', '18:00:00', '23:00:00');