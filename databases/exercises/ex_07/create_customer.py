import os
import psycopg2
from dotenv import load_dotenv

# Load environment variables
load_dotenv()


def create_customer(customer_name, description):
    """Create customer in the table using customer_name and description."""
                
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
        
        # Execute the Delete statements
        cur.execute("INSERT INTO  customers(customer_name, industry) VALUES (%s, %s)", (customer_name, description))
        
        # Commit the changes to the database
        conn.commit()

        cur.execute("SELECT * FROM customers WHERE customer_name=%s AND industry=%s", (customer_name, description))

        row = cur.fetchone()
        
        # Close communication with the PostgreSQL database
        cur.close()

        return str(row)

        # return str(' '.join(str(i) for i in row))
        
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
        
    finally:
        if conn is not None:
            conn.close()


print(create_customer('Jhonty Rhodes', 'Entertainment'))
