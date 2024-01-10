# Connecting to PostgreSQL Server through Python

## Create and activate virtual environment

```
# Create virtual environment
python3 -m venv .venv

# Activate virtual environment
# Linux
source .venv/bin/activate

# Windows
call .venv/Scripts/activate

# Add .venv/ to .gitignore
```

## Install python-dotenv - environment variable manager

```
pip install python-dotenv
```

## Install psycopg2 - Python PostgreSQL connector

```
pip install psycopg2

# OR

pip install psycopg2-binary
```

> pip freeze > requirements.txt

## Create a database

```
sudo su postgres

psql
```

1. Create a new user

    ```
    CREATE USER <username> WITH LOGIN CREATEDB PASSWORD '<password>';
    ```

2. Set role to created user

    ```
    SET ROLE <username>;

    # Confirm role change
    SELECT current_user;
    ```

3. Create a new db

    ```
    CREATE DATABASE <db name>;

    # Check if db has been created 
    \l 
    ```

## Connect to database

1. Create a file called `connect.py` and add the following code:

    ```python
    import psycopg2
    import os
    from dotenv import load_dotenv

    # Load all environment variables from .env file
    load_dotenv()


    def connect():
        """Connecting to the PostgreSQL Server"""
        conn = None
        
        try:
            # connect to the PostgreSQL Server
            print("Connecting to the PostgreSQL Database")
            conn = psycopg2.connect(
                host=os.environ.get("DB_HOST"),
                database=os.environ.get("DB_NAME"),
                user=os.environ.get("DB_USER"),
                password=os.environ.get("DB_PASSWORD"),
                port=os.getenv("DB_PORT")
            )
            
            # Create a cursor
            cur = conn.cursor()
            
            # Excute a statement
            cur.execute("SELECT version();")
            
            # Display the database
            print(cur.fetchone())
            cur.fetchall()
            cur.fetchmany(size=10)
            
            # Close the connection
            cur.close()
            
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
            
        finally:
            if conn is not None:
                conn.close()
                print("Database connection closed!")
    ```


- Perform CRUD operations

## psycopg2 Functions

| Function | Description |
|----------|-------------|	
| `psycopg2.connect(database="testdb", user="postgres", password="cohondob", host="127.0.0.1", port="5432")` | This API opens a connection to the PostgreSQL database. If database is opened successfully, it returns a connection object. |
|  `connection.cursor()` | This routine creates a cursor which will be used throughout of your database programming with Python. |
| `cursor.execute(sql [, optional parameters])` | This routine executes an SQL statement. The SQL statement may be parameterized (i.e., placeholders instead of SQL literals). The psycopg2 module supports placeholder using %s sign. For example: `cursor.execute("insert into people values (%s, %s)", (who, age))` |
| `cursor.executemany(sql, seq_of_parameters)` | This routine executes an SQL command against all parameter sequences or mappings found in the sequence sql. |
| `cursor.callproc(procname[, parameters])` | This routine executes a stored database procedure with the given name. The sequence of parameters must contain one entry for each argument that the procedure expects. |
| `cursor.rowcount` | This read-only attribute which returns the total number of database rows that have been modified, inserted, or deleted by the last last execute*(). |
| `connection.commit()` | This method commits the current transaction. If you do not call this method, anything you did since the last call to commit() is not visible from other database connections. |
| `connection.rollback()` | This method rolls back any changes to the database since the last call to commit(). |
| `connection.close()` | This method closes the database connection. Note that this does not automatically call commit(). If you just close your database connection without calling commit() first, your changes will be lost! |
| `cursor.fetchone()` | This method fetches the next row of a query result set, returning a single sequence, or None when no more data is available. |
| `cursor.fetchmany([size=cursor.arraysize])` | This routine fetches the next set of rows of a query result, returning a list. An empty list is returned when no more rows are available. The method tries to fetch as many rows as indicated by the size parameter. |
| `cursor.fetchall()` | This routine fetches all (remaining) rows of a query result, returning a list. An empty list is returned when no rows are available. |