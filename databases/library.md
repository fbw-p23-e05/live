# Library Management Database

1. Write an SQL script that creates a database called `library_management` with the following tables:

    a. Authors:
        - author_id (Primary Key) Auto incremented
        - author_name (string)
        - date_of_birth (date)
        - place of birth (string)
        - genre (string)

    b. Books:
        - book_id (Primary Key) Auto incremented
        - book_name (string)
        - description (string)
        - genre (string)
        - units_sold (integer)
        - price (decimal)
        - author_id (Foreign Key)

2. Write an SQL script to add at least 10 records to each of these tables in the database.

    > Execute both scripts using your preferred tool, DBeaver or psql.

3. Write a query to retrieve all books written by a specific author.
4. Select all books from the same genre.
5. Select authors from more the same genre.

