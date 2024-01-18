SELECT art_piece_name, description, price
FROM art_pieces
WHERE art_piece_id IN 
	(
		SELECT art_piece_id
		FROM art_pieces
		WHERE price < 1000000.00;
	);

