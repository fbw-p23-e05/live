

import os
import psycopg2
from dotenv import load_dotenv

# Load environment variables
load_dotenv()


def update_vendor(vendor_id, **kwargs):
    """Update vendor in the table using vendor_id and **kwargs."""
                
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

        # new = list(k for k in kwargs.keys())
        # new = tuple((k, j) for k, j in (kwargs.keys(), kwargs.values()))
        # emp = []
        # for part in new:
        #     for second_part in part:
        #         emp.append(second_part)
        # tup = tuple(emp)
        # print(tup)


        # cur.execute("UPDATE vendors SET %s=%s, %s=%s WHERE vendor_id=%s", (tuple((kwarg for kwarg in kwargs.values())) + (vendor_id,)))

        # cur.execute('UPDATE vendors SET %s=%s, %s=%s WHERE vendor_id=%s', (tup + (vendor_id,)))

        # cur.execute("UPDATE vendors SET %s, %s WHERE vendor_id=%s", tup + (vendor_id,))

        cur.execute("UPDATE vendors SET {}=%s, {}=%s WHERE vendor_id=%s".format(*list(kwarg for kwarg in kwargs.keys())), tuple((kwarg for kwarg in kwargs.values())) + (vendor_id,))



        # cur.execute('Update vendors set %s where vendor_id=%s', ', '.join(k+'="'+v+'"' for k, v in kwargs.items()), vendor_id)
        # cur.execute("DELETE FROM products WHERE product_id=%s", (product_id,))
        
        # Execute the Delete statements
        # cur.execute("INSERT INTO  customers(customer_name, industry) VALUES (%s, %s)", (customer_name, description))
        
        # Commit the changes to the database
        conn.commit()

        cur.execute("SELECT * FROM vendors WHERE vendor_id = %s", (vendor_id,))


        row = cur.fetchone()
        
        # Close communication with the PostgreSQL database
        cur.close()

        # return str(row)

        return str(' '.join(str(i) for i in row))
        
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
        
    finally:
        if conn is not None:
            conn.close()


# print(create_customer('Jhonty Rhodes', 'Entertainment'))
print(update_vendor(3, vendor_name='Lenovo', industry='Electronics'))


