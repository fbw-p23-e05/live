SELECT SUM(price) AS total_value_of_pieces
FROM art_pieces;

SELECT artist_id, SUM(price) AS total_value_of_pieces_by_artist
FROM art_pieces
GROUP BY artist_id
ORDER BY artist_id;
