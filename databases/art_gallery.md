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
    ```
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


## Alter the database to add new fields

```
ALTER TABLE <table name>
ALTER COLUMN <column name> [SET DATA] TYPE <new data type>;
```
