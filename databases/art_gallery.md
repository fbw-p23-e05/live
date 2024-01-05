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
    -- Create artists and art pieces tables
    -- Establish Foreign Key Relationship between both tables using artist_id field
    DROP TABLE IF EXISTS art_pieces;
    DROP TABLE IF EXISTS artists;

    CREATE TABLE IF NOT EXISTS artists(
        artist_id SERIAL PRIMARY KEY,
        first_name TEXT NOT NULL,
        last_name TEXT,
        email_address VARCHAR(100) UNIQUE NOT NULL,
        art_style TEXT NOT NULL,
        date_of_birth DATE,
        UNIQUE(first_name, last_name)
    );

    CREATE TABLE IF NOT EXISTS art_pieces(
        art_piece_id SERIAL PRIMARY KEY,
        art_piece_name TEXT UNIQUE NOT NULL, -- COLUMN Constraint
        description TEXT,
        date_of_creation DATE,
        genre TEXT NOT NULL,
        price DECIMAL NOT NULL,
        artist_id INT NOT NULL REFERENCES artists(artist_id) ON DELETE SET NULL,
        UNIQUE(artist_id, art_piece_name) -- TABLE constraint
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
    VALUES ('', 'Brown', 'jbrown@mail.com', 'Doodler', '2001-09-15')
    ON CONFLICT DO NOTHING;
            
    INSERT INTO art_pieces(
        art_piece_name,
        description,
        date_of_creation,
        genre,
        price,
        artist_id
    )
    VALUES ('Mona Lisa', 'Painting of beautiful woman.', '1503-12-01', 'Renaissance', 860000000, 5)
    ON CONFLICT DO NOTHING;
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


- Handling database/table duplication
- Ensuring uniqueness of records
- Handling null columns/cells
