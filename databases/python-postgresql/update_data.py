import os
import psycopg2
from dotenv import load_dotenv

# Load environment variables
load_dotenv()


def update_vendor():
    """Update vendors in the table."""
    sql = """UPDATE vendors
                SET vendor_name = 'The Pharmaceutical Group'
                WHERE vendor_id = 2;"""
                
    conn = None
    try:
        
        # Create connection
        print("Establishing database connection...")
        conn = psycopg2.connect(
            host=os.getenv("DB_HOST"),
            database=os.getenv("DB_NAME"),
            user=os.getenv("DB_USER"),
            password=os.getenv("DB_PASSWORD"),
            port=os.getenv("DB_PORT")
        )
        
        # Create a cursor
        cur = conn.cursor()
        
        # Execute the update statements
        cur.execute(sql)
        
        # Commit the changes to the database
        conn.commit()
        
        # Close communication with the PostgreSQL database
        cur.close()
        
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
        
    finally:
        if conn is not None:
            conn.close()


if __name__ == '__main__':
    update_vendor()
    