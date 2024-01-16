ALTER TABLE artists 
ADD COLUMN phone_numbers TEXT [];

INSERT INTO artists (
	first_name,
	last_name,
	email_address,
	art_style,
	date_of_birth,
	phone_numbers
)
VALUES ('David', 'Johnson', 'djohnson@art.com', 'Painter',
		'1978-02-05', ARRAY ['+978542158765', '+4598784215464', '+260987974156']);

UPDATE artists
SET phone_numbers = ARRAY ['+874551224784', '+65254788712']
WHERE artist_id = 2;

SELECT first_name, phone_numbers[2] FROM artists;



