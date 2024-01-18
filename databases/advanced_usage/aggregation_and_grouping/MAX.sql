SELECT MAX(art_piece_name) AS highest_piece_name
FROM art_pieces;

SELECT MAX(price) AS highest_price
FROM art_pieces;

SELECT MAX(end_at) AS last_call_time
FROM shifts;