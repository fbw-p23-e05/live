-- Database creation
CREATE DATABASE fruit_baskets;

-- Table Creation
CREATE TABLE IF NOT EXISTS basket_a(
	a_id SERIAL PRIMARY KEY,
	fruit_a VARCHAR(100) NOT NULL
);

CREATE TABLE IF NOT EXISTS basket_b(
	b_id SERIAL PRIMARY KEY,
	fruit_b VARCHAR(100) NOT NULL
);

-- Data insertion
INSERT INTO basket_a(fruit_a)
VALUES 
	('Apple'),
	('Orange'),
	('Mango'),
	('Banana'),
	('Cucumber');

INSERT INTO basket_b(fruit_b)
VALUES 
	('Orange'),
	('Litchi'),
	('Banana'),
	('Grapes'),
	('Mango');
