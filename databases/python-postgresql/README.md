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