--CREATE TYPE stars 
--AS ENUM ('1 star', '2 stars', '3 stars', '4 stars', '5 stars');
--
--ALTER TABLE art_pieces 
--ADD COLUMN rating stars;

INSERT INTO art_pieces (
	art_piece_name,
	description,
	date_of_creation,
	genre,
	price,
	artist_id,
	rating
)
VALUES ('Painting of the sky.', 'A large painting of a blue sky', 
		'2020-09-10', 'Realism', 50000.00, 1, '6 stars');


