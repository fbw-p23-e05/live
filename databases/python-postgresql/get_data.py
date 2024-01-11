import os
import psycopg2
from dotenv import load_dotenv

# Load environmnent variables
load_dotenv()


def get_vendors():
    """Query data from tye vendors table."""
    
    conn = None
    
    try:
        # Create the database connection.
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
        
        cur.execute("SELECT * FROM vendors ORDER BY vendor_name;")

        # create list of results
        # data = cur.fetchone()[1]  # Returns a tuple
        # print(data)
        
        # data_1 = cur.fetchmany(size=2)
        # print(data_1)
        
        data_2 = cur.fetchall()  # Returns list of tuple
        print(data_2)
        
        # Close the database communication
        cur.close()
        
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
        
    finally:
        if conn is not None:
            conn.close()
            

if __name__ == '__main__':
    get_vendors()
