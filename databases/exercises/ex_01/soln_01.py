
import sqlite3


conn = sqlite3.connect('test.db')

cursor = conn.cursor()

# sql_script = '''CREATE TABLE student(
# student_name TEXT not null,
# course_name TEXT not null);'''


# sql_script = '''INSERT INTO student
# (student_name, course_name) values
# ('Lisa', 'Python');'''

sql_script = 'SELECT * FROM student;'

cursor.execute(sql_script)

table = cursor.fetchall()

# print(f'Result from DB for student table:  {table}')

for row in table:
    print(row)

# conn.commit()

# conn.close()









