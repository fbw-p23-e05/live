-- Create artists and art pieces tables
-- Establish Foreign Key Relationship between both tables using artist_id field
DROP TABLE IF EXISTS art_pieces;
DROP TABLE IF EXISTS artists;

CREATE TABLE IF NOT EXISTS artists(
    artist_id SERIAL PRIMARY KEY,
    first_name TEXT NOT NULL,
    last_name TEXT,
    email_address VARCHAR(100) UNIQUE NOT NULL,
    art_style TEXT NOT NULL,
    date_of_birth DATE,
    UNIQUE(first_name, last_name)
);

CREATE TABLE IF NOT EXISTS art_pieces(
    art_piece_id SERIAL PRIMARY KEY,
    art_piece_name TEXT UNIQUE NOT NULL, -- COLUMN Constraint
    description TEXT,
    date_of_creation DATE,
    genre TEXT NOT NULL,
    price DECIMAL NOT NULL,
    artist_id INT NOT NULL REFERENCES artists(artist_id) ON DELETE SET NULL,
    UNIQUE(artist_id, art_piece_name) -- TABLE constraint
);
