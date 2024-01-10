

# Task 1
CREATE DATABASE map;

\c map (Does not work on DBeaver)

CREATE TABLE country(
id SERIAL PRIMARY KEY,
name VARCHAR(30),
population INT,
last_status_change DATE
);


INSERT INTO country(
name, population, last_status_change) VALUES
('Germany', 83190556, '1990-10-03'),
('France', 67413000, '1958-10-04');

SELECT * FROM country;

# Task 2
CREATE TABLE IF NOT EXISTS city(
id SERIAL PRIMARY KEY,
name VARCHAR(30),
area DECIMAL,
is_capital BOOLEAN,
country_id INT REFERENCES country(id) ON DELETE SET NULL 
);


INSERT INTO city(
name, area, is_capital, country_id) VALUES
('Berlin', 891.7, true, 1),
('Marseille', 240.62, false, 2);

SELECT * FROM city;

# Task 3
SELECT * FROM city, country WHERE city.country_id=country.id;

# Task 4
SELECT * FROM city, country WHERE city.country_id = country.id 

AND country.name = 'Germany';

# Task 5

SELECT country.name, city.name, city.area FROM city, country WHERE city.country_id = country.id 

ORDER BY city.area

LIMIT 1;

# Task 6

SELECT country.name, city.name, city.area FROM city, country WHERE city.country_id = country.id 

AND city.is_capital = TRUE

ORDER BY city.area

LIMIT 1;


# Task 7

SELECT city.name, country.name, country.population FROM city, country WHERE city.country_id = country.id 

AND city.is_capital = TRUE

ORDER BY country.population DESC 

LIMIT 3;

# Task 8

DELETE FROM country WHERE name='Germany';

SELECT * FROM city;

# Task 9

ALTER TABLE country ADD COLUMN code CHAR(2) UNIQUE;

\i country.sql

SELECT name, code FROM country;

\i country_test.sql


# Task 10

CREATE TABLE language(
code CHAR(2) PRIMARY KEY,
name VARCHAR(50));

\i language.sql

SELECT name, code FROM language;


\i language_test.sql


# Task 11

DROP TABLE IF EXISTS locale;

CREATE TABLE locale(
name VARCHAR(30),
language_code CHAR(2) REFERENCES language(code),
country_code CHAR(2) REFERENCES country(code),
PRIMARY KEY (language_code, country_code)
);

\i locale.sql

SELECT * FROM locale;

\i locale_test.sql

# Task 12

SELECT locale.name AS "Locale",
country.name AS "country",
language.name AS "Language" FROM 
locale, country, language
WHERE locale.language_code=language.code
AND locale.country_code=country.code
ORDER BY language.name;



