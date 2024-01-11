# Task 1
\i movies.sql

CREATE VIEW long_movies AS 

SELECT * FROM movies 
WHERE runtime > 150 
ORDER BY runtime DESC;

SELECT * FROM long_movies;

# Task 2

CREATE VIEW short_trailers AS 

SELECT * FROM trailers 
WHERE length <= 2;

SELECT * FROM short_trailers;

# Task 3

SELECT long_movies.title, short_trailers.url
FROM long_movies, short_trailers
WHERE long_movies.id = short_trailers.movie_id;


# Task 4

SELECT movies.title, trailers.url
FROM movies, trailers
WHERE movies.id = trailers.movie_id 
AND movies.runtime > 150
AND trailers.length <= 2
ORDER BY runtime DESC;


# Task 5

CREATE VIEW long_movies_with_short_trailers AS 
SELECT long_movies.title, short_trailers.url
FROM long_movies, short_trailers
WHERE long_movies.id = short_trailers.movie_id;

SELECT * FROM long_movies_with_short_trailers;

CREATE VIEW top_rated_long_movies AS
SELECT * FROM long_movies 
WHERE rating > 4;

SELECT * FROM top_rated_long_movies;

CREATE OR REPLACE VIEW long_movies AS 

SELECT * FROM movies
WHERE runtime > 120;

SELECT * FROM top_rated_long_movies;

SELECT * FROM long_movies_with_short_trailers;


# Task 6

DROP VIEW top_rated_long_movies;

CREATE MATERIALIZED VIEW top_rated_long_movies AS 
SELECT * FROM long_movies 
WHERE rating > 4;

SELECT * FROM top_rated_long_movies;


CREATE OR REPLACE VIEW long_movies AS 

SELECT * FROM movies 
WHERE runtime > 150 
ORDER BY runtime DESC;

REFRESH MATERIALIZED VIEW top_rated_long_movies;

SELECT * FROM top_rated_long_movies;

