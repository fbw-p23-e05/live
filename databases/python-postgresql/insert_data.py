import os
import psycopg2
from dotenv import load_dotenv

# Load environment variables
load_dotenv()


def insert_data():
    """Insert data into the created tables."""
    
    sql = [
        """
        INSERT INTO vendors(
            vendor_name,
            industry
        )
        VALUES ('RG Manufacturing', 'Manufacturing'),
                ('PK Pharmaceuticals', 'Pharmaceutical'),
                ('X Motors', 'Vehicles');
        """,
        """
        INSERT INTO products(
            product_name,
            description,
            vendor_id
        )
        VALUES ('Paracetamol', 'Painkiller', 2),
                ('CyberTruck', 'Electric flatbed truck', 3),
                ('Steel rods', 'Steel for building use.', 1);
        """,
        """
        INSERT INTO customers(
            customer_name,
            industry
        )
        VALUES ('Blue Cat Inc.', 'Transportation');
        """
    ]
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
        
        # Execute the Insertion statements
        for command in sql:
            cur.execute(command)
        
        # Commit the changes
        conn.commit()
        
        # Close communication with database
        cur.close()
    
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
        
    finally:
        if conn is not None:
            print("Closing database connection...")
            conn.close()
            

if __name__ == '__main__':
    insert_data()
    