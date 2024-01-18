SELECT MIN(price) AS lowest_price
FROM art_pieces;

SELECT MIN(art_piece_name) AS lowest_piece_name
FROM art_pieces;

SELECT MIN(start_at) AS first_call
FROM shifts;

SELECT MIN(date_of_creation) AS oldest_piece
FROM art_pieces;