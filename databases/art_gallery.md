# Art Gallery Database

1. Artists:
    - first name (String)
    - last name (String)
    - email address (String)
    - style (string)
    - date of birth (date)

2. Art Pieces:
    - artist (Foreign Key)
    - name (string)
    - date of creation (date)
    - genre (string)
    - price (decimal)

## Create a user

```
CREATE USER <name> WITH PASSWORD '<password>';
```

## assign the user privileges

```
# Database creation privileges
ALTER USER <username> WITH CREATEDB;
```

## Switch role to the created user

```
SET ROLE <username>;

# Check current user
SELECT current_user;
```

## Create the art gallery database 

```
CREATE DATABASE <db name>;
```


## Connect to database

```
\c <db name>

# Change role
SET ROLE <username>
```

## Create the tables

1. Create the following script and save it.
    ```sql
    CREATE TABLE artists(
        artist_id INT PRIMARY KEY,
        first_name TEXT,
        last_name TEXT,
        email_address VARCHAR(100),
        art_style TEXT,
        date_of_birth DATE
    );

    CREATE TABLE art_pieces(
        art_piece_id INT PRIMARY KEY,
        art_piece_name TEXT,
        description TEXT,
        date_of_creation DATE,
        genre TEXT,
        price DECIMAL,
        artist_id INT REFERENCES artists(artist_id)
    );
    ```

2. From the command line run the script with the following command:

    ```
    \i '<path>\<to>\<script>'
    ```

## Add data into the database

1. Create the following script and save it.

    ```sql
    INSERT INTO artists(
        first_name,
        last_name,
        email_address,
        art_style,
        date_of_birth
    )
    VALUES ('Pablo', 'Picasso', 'ppicasso@gmail.com', 'Expressionist', '1881-10-25'),
            ('Vincent', 'van Gogh', 'vvangogh@gmail.com', 'Post-Impressionist', '1853-03-30'),
            ('Claude', 'Monet', 'cmonet@gmail.com', 'Impressionist', '1840-11-14');
            

    INSERT INTO art_pieces(
        art_piece_name,
        description,
        date_of_creation,
        genre,
        price,
        artist_id
    )
    VALUES ('The Self-Portrait', 'Painting of himself.', '1889-09-01', 'Post-Impressionism', 120000000.00, 2),
            ('The Old Guitarist', 'Elderly guitar player on the street', '1904-03-01', 'Expressionism', 100000000.00, 1),
            ('The Water Lily Pond', 'A painting of a pond.', '1899-12-01', 'Impressionism', 70400000.00, 3);
    ```

2. From the command line run the script with the following command:

    ```
    \i '<path>\<to>\<script>'
    ```


## Alter the database to add new fields

```
ALTER TABLE <table name>
ALTER COLUMN <column name> [SET DATA] TYPE <new data type>;
```
