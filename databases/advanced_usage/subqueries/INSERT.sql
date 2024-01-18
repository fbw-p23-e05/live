INSERT INTO art_pieces_bkp 
SELECT * 
FROM art_pieces
WHERE art_piece_id IN (
	SELECT art_piece_id
	FROM art_pieces
);