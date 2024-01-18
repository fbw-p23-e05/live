SELECT artist_id, AVG(price) AS avg_price
FROM art_pieces
GROUP BY artist_id;

SELECT ROUND(AVG(price), 2) AS avg_price
FROM art_pieces;