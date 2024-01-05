INSERT INTO artists(
	first_name,
    last_name,
    email_address,
    art_style,
    date_of_birth
)
VALUES ('', 'Brown', 'jbrown@mail.com', 'Doodler', '2001-09-15')
ON CONFLICT DO NOTHING;
        
INSERT INTO art_pieces(
    art_piece_name,
    description,
    date_of_creation,
    genre,
    price,
    artist_id
)
VALUES ('Mona Lisa', 'Painting of beautiful woman.', '1503-12-01', 'Renaissance', 860000000, 5)
ON CONFLICT DO NOTHING;