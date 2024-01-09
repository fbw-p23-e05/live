-- Selecting all art pieces with a price greater than or equal to 100million
SELECT * FROM art_pieces
WHERE price >= 100000000.00;

-- Creating the view for the query
CREATE VIEW pricey_pieces AS
	SELECT * FROM art_pieces
	WHERE price >= 100000000.00; 
	
-- Interact with the query
SELECT * FROM pricey_pieces; --public.pricey_pieces

-- Modifying the view
CREATE OR REPLACE VIEW pricey_pieces AS 
	SELECT *
	FROM art_pieces
	
	
	WHERE price >= 150000000.00;
	
-- Changing view name
ALTER VIEW pricey_pieces RENAME TO pricey_art_pieces;

-- Creating a view from an existing view
CREATE VIEW artist_contacts AS
	SELECT first_name, email_address 
	FROM artist_dets;
	
-- Dropping a view that other views depend on
DROP VIEW artist_dets CASCADE;

-- Dropping a view if it exists
DROP VIEW IF EXISTS artist_dets CASCADE;

-- Dropping a view
DROP VIEW IF EXISTS pricey_pieces;

-- Create updatable views
CREATE VIEW old_age_artist_contacts AS 
	SELECT first_name, email_address
	FROM artists
	WHERE date_of_birth < '1900-01-01';
	
-- Add a new artist
INSERT INTO artists(
	first_name,
	last_name,
	email_address,
	art_style,
	date_of_birth
)
VALUES ('Mary', 'Josephs', 'mjosephs@artistry.com', 'Painting', '1897-02-25');

-- Create a non-updatable view
CREATE VIEW paintings_value AS
	SELECT 
		art_piece_name, 
		description, 
		date_of_creation, 
		genre, 
		SUM(price) AS total_value 
	FROM art_pieces
	GROUP BY 
		art_piece_name,
		description,
		date_of_creation,
		genre;
	
DELETE FROM paintings_value
WHERE genre = 'Doodling';