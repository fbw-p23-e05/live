import os
import psycopg2
from dotenv import load_dotenv

# Load environment variables
load_dotenv()


def create_tables():
    """Create tables in the database."""
    
    commands = [
        """
        CREATE TABLE vendors(
            vendor_id SERIAL PRIMARY KEY,
            vendor_name VARCHAR(200) NOT NULL,
            industry VARCHAR(100)
        );
        """,
        """
        CREATE TABLE products(
            product_id SERIAL PRIMARY KEY,
            product_name VARCHAR(100) NOT NULL,
            description TEXT,
            vendor_id INT,
            FOREIGN KEY (vendor_id)
                REFERENCES vendors(vendor_id)
                ON UPDATE CASCADE ON DELETE CASCADE
        );
        """,
        """
        CREATE TABLE customers(
            customer_id SERIAL PRIMARY KEY,
            customer_name VARCHAR(200) NOT NULL,
            industry VARCHAR
        );
        """
    ]
    conn = None
    
    try:
        # Connect to the PostgreSQL Server
        print("Establishing Database connection...")
        conn = psycopg2.connect(
            host=os.getenv("DB_HOST"),  # os.environ.get("DB_HOST")
            database=os.getenv("DB_NAME"),
            user=os.getenv("DB_USER"),
            password=os.getenv("DB_PASSWORD"),
            port=os.getenv("DB_PORT")
        )
        
        # Create a cursor
        print("Creating cursor...")
        cur = conn.cursor()
        
        # Create the tables one by one
        counter = 0
        for command in commands:
            counter += 1
            print("Executing command", counter)
            cur.execute(command)
            
        # Close communication with the PostgreSQL database server
        print("Closing cursor...")
        cur.close()
        
        # Commit the changes
        print("Commiting changes to database...")
        conn.commit()
        
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
        
    finally:
        if conn is not None:
            print("Closing database connection...")
            conn.close()
    
            
if __name__ == '__main__':
    create_tables()
        