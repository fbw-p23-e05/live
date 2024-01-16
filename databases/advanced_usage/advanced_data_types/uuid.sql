-- Create the extension
CREATE EXTENSION IF NOT EXISTS "uuid-ossp";

--SELECT uuid_generate_v4();

 -- Create a table with uuid primary key column
CREATE TABLE museums (
	location_id uuid DEFAULT uuid_generate_v4(),
	location_name TEXT,
	phone_number TEXT,
	PRIMARY KEY(location_id)
);

INSERT INTO museums (
	location_name,
	phone_number
)
VALUES ('The Old Age Museum', '+78958456235');

ALTER TABLE art_pieces 
ADD COLUMN museum_id uuid REFERENCES museums(location_id);

INSERT INTO art_pieces (
	art_piece_name,
	description,
	date_of_creation,
	genre,
	price,
	artist_id,
	rating,
	museum_id
)
VALUES ('The painted dog.', 'Portrait of dog that splashed itself with paint.',
		'2023-10-10', 'Paintings', 100000.00, 9, '4 stars', 
		'f5424b56-cc46-4361-82b4-a992e4d25596');



