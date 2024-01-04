-- Create artists and art pieces tables
-- Establish Foreign Key Relationship between both tables using artist_id field
CREATE TABLE artists(
	artist_id SERIAL PRIMARY KEY,
	first_name TEXT,
    last_name TEXT,
    email_address VARCHAR(100),
    art_style TEXT,
    date_of_birth DATE
);

CREATE TABLE art_pieces(
	art_piece_id SERIAL PRIMARY KEY,
    art_piece_name TEXT,
    description TEXT,
    date_of_creation DATE,
    genre TEXT,
    price DECIMAL,
    artist_id INT REFERENCES artists(artist_id)
);
