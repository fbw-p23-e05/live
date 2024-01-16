
-- Task 1

/*SELECT student.name AS "Student", mentor.name AS "Mentor",
student.city AS "Student’s city",
mentor.city AS "Mentor’s city"
FROM student
JOIN mentor
ON mentor.id = student.mentor_id
ORDER BY student.name;*/

-- Task 2

/*SELECT student.name AS "Student", mentor.name AS "Mentor",
student.city AS "Student’s city",
mentor.city AS "Mentor’s city"
FROM student LEFT JOIN mentor
ON mentor.id = student.mentor_id
ORDER BY student.name;*/

-- Task 3

/*SELECT mentor.name AS "Mentor",
student.name AS "Student",
mentor.city AS "Mentor’s city",
student.city AS "Student’s city"
FROM student RIGHT JOIN mentor
ON mentor.id = student.mentor_id
ORDER BY mentor.name;*/

-- Task 4

/*SELECT mentor.name AS "Mentor",
student.name AS "Student",
mentor.city AS "Mentor’s city",
student.city AS "Student’s city"
FROM student JOIN mentor
ON mentor.id = student.mentor_id
WHERE student.city = 'Berlin'
OR mentor.city = 'Berlin'
ORDER BY mentor.name;*/


-- Task 5

/*SELECT student.name AS "Student",
student.city AS "Student’s city",
mentor.name AS "Mentor"
FROM student JOIN mentor
ON mentor.city = student.city
ORDER BY student.city, student.name, mentor.name;*/

-- Task 6

/*UPDATE student SET local_mentor = mentor.id
FROM mentor 
WHERE mentor.city = student.city;*/

SELECT * FROM student
ORDER BY name;








