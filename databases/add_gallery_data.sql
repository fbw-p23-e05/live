INSERT INTO artists(
	first_name,
	last_name,
	email_address,
	art_style,
	date_of_birth
)
VALUES ('Pablo', 'Picasso', 'ppicasso@gmail.com', 'Expressionist', '1881-10-25'),
		('Vincent', 'van Gogh', 'vvangogh@gmail.com', 'Post-Impressionist', '1853-03-30'),
		('Claude', 'Monet', 'cmonet@gmail.com', 'Impressionist', '1840-11-14');
		

INSERT INTO art_pieces(
	art_piece_name,
	description,
	date_of_creation,
	genre,
	price,
	artist_id
)
VALUES ('The Self-Portrait', 'Painting of himself.', '1889-09-01', 'Post-Impressionism', 120000000.00, 2),
		('The Old Guitarist', 'Elderly guitar player on the street', '1904-03-01', 'Expressionism', 100000000.00, 1),
		('The Water Lily Pond', 'A painting of a pond.', '1899-12-01', 'Impressionism', 70400000.00, 3);