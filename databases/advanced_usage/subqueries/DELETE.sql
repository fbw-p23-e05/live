DELETE FROM art_pieces_bkp 
WHERE art_piece_id IN (
	SELECT art_piece_id
	FROM art_pieces
	WHERE artist_id = 1
);