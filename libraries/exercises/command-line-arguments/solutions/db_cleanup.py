import sys

args = sys.argv[1:]
 
for db_name in args:
    # Database operations to be performed
    print(f"Database {db_name} has been cleaned.")
    