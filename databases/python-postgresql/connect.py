import psycopg2
import os
from dotenv import load_dotenv

# Load all environment variables from .env file
load_dotenv()


def connect():
    """Connecting to the PostgreSQL Server"""
    conn = None
    
    try:
        # Connect to the PostgreSQL Server
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
        
        # Execute a statement
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
            