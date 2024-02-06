-- Task 1

CREATE DATABASE webinars;

\c webinars;

\i data/tables.sql

\timing;

\i data/data.sql

-- Performance times

-- Task 2

COPY teacher TO '/home/DCI/Python/DB Performance/teacher.csv';
COPY student TO '/home/DCI/Python/DB Performance/student.csv';
COPY webinar TO '/home/DCI/Python/DB Performance/webinar.csv';
COPY registration TO '/home/DCI/Python/DB Performance/registration.csv';


-- Task 3

BEGIN;
  TRUNCATE TABLE teacher, student, webinar, registration CASCADE;

  COPY teacher FROM '/home/DCI/Python/DB Performance/teacher.csv';
  COPY student FROM '/home/DCI/Python/DB Performance/student.csv';
  COPY webinar FROM '/home/DCI/Python/DB Performance/webinar.csv';
  COPY registration FROM '/home/DCI/Python/DB Performance/registration.csv';
COMMIT;


-- Task 4

BEGIN;
  -- Clear data
  TRUNCATE TABLE teacher, student, webinar, registration CASCADE;

  -- Remove constraints
  -- We remove all the PKEY constraints using CASCADE. This will remove
  -- also the related foreign key.
  ALTER TABLE teacher DROP CONSTRAINT teacher_pkey CASCADE;
  ALTER TABLE student DROP CONSTRAINT student_pkey CASCADE;
  ALTER TABLE webinar DROP CONSTRAINT webinar_pkey CASCADE;
  ALTER TABLE registration DROP CONSTRAINT registration_pkey CASCADE;

  -- Load data
  COPY teacher FROM '/home/DCI/Python/DB Performance/teacher.csv';
  COPY student FROM '/home/DCI/Python/DB Performance/student.csv';
  COPY webinar FROM '/home/DCI/Python/DB Performance/webinar.csv';
  COPY registration FROM '/home/DCI/Python/DB Performance/registration.csv';

  -- Add constraints again
  ALTER TABLE teacher ADD CONSTRAINT teacher_pkey PRIMARY KEY(id);
  ALTER TABLE student ADD CONSTRAINT student_pkey PRIMARY KEY(id);
  ALTER TABLE student ADD CONSTRAINT student_teacher_fkey
      FOREIGN KEY(mentor_id) REFERENCES teacher;
  ALTER TABLE webinar ADD CONSTRAINT webinar_pkey PRIMARY KEY(id);
  ALTER TABLE webinar ADD CONSTRAINT webinar_teacher_fkey
      FOREIGN KEY(teacher_id) REFERENCES teacher;
  ALTER TABLE registration ADD CONSTRAINT registration_pkey PRIMARY KEY(id);
  ALTER TABLE registration ADD CONSTRAINT registration_student_fkey
      FOREIGN KEY(student_id) REFERENCES student;
  ALTER TABLE registration ADD CONSTRAINT registration_webinar_fkey
      FOREIGN KEY(webinar_id) REFERENCES webinar;
COMMIT;




-- Task 5

SELECT * FROM student, teacher
WHERE student.mentor_id = teacher.id
AND (student.city = 'Berlin' OR teacher.city = 'Berlin');

-- Or 

SELECT * FROM student JOIN teacher
ON student.mentor_id = teacher.id
WHERE student.city = 'Berlin' OR teacher.city = 'Berlin';



-- Task 6

CREATE INDEX ON student(city);
CREATE INDEX ON registration(date);


-- Task 7

CREATE INDEX ON teacher(City);

SELECT ANALYZE SELECT * FROM student
WHERE city = ANY(ARRAY(SELECT DISTINCT city FROM teacher));


-- Task 8

-- This should be a python file.
"""Print the students and mentors."""
import psycopg2
import datetime
import os


connection = psycopg2.connect(
            host=os.getenv("DB_HOST"),
            database=os.getenv("DB_NAME"),
            user=os.getenv("DB_USER"),
            password=os.getenv("DB_PASSWORD"),
            port=os.getenv("DB_PORT")
        )

cursor = connection.cursor()

params = {
    "date": "2021-01-01",
    "topic": "Django"
}

start = datetime.datetime.now()

cursor.execute("SELECT student.name, teacher.name FROM student "
               "JOIN registration ON student.id = registration.student_id "
               "JOIN webinar ON webinar.id = registration.webinar_id "
               "JOIN teacher ON teacher.id = student.mentor_id "
               f"WHERE date > '{params['date']}' "
               f"AND webinar.name LIKE '%{params['topic']}%' "
               "ORDER BY student.id;")

with open("students_query.csv", "w") as file:
    file.write("Student,Teacher\n")
    for student in cursor.fetchall():
        file.write(f"{student[0]},{student[1]}\n")

end = datetime.datetime.now()
print(f"It took {end - start}")
connection.close()

