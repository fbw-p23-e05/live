# Task 1

CREATE DATABASE library_management;

\c library_management


CREATE TABLE authors(author_id SERIAL PRIMARY KEY, author_name VARCHAR(50),
date_of_birth DATE, place_of_birth VARCHAR(30), genre VARCHAR(20));


CREATE TABLE books(book_id SERIAL PRIMARY KEY, book_name VARCHAR(50), description TEXT, genre VARCHAR(20), units_sold INT, price DECIMAL, author_id INT REFERENCES authors(author_id));

# Task 2

INSERT INTO authors(author_name, date_of_birth, place_of_birth, genre) VALUES 
('Mike Pascal', '1992-05-22', 'Berlin', 'Science'),
('Tom Brandoll', '1984-08-11', 'Boston', 'Fiction');


INSERT INTO books(book_name, description, genre, units_sold, price, author_id) VALUES 
('Organic Chemistry', 'This is a popular chemistry book', 'Science', 997, 234.55, 1),
('Life on the Mars', 'This book is all about surviving on Mars', 'Fiction', 2242, 180.33, 2);

# Task 3

SELECT books.book_name FROM books, authors WHERE authors.author_id = books.author_id AND authors.author_name='Mike Pascal';

# Task 4

SELECT * FROM authors WHERE genre='Fiction';

# Task 5

SELECT * FROM books WHERE genre='Fiction';