

-- Task 1

/*SELECT student.name AS "Student",
mentor.name AS "Mentor",
loc_mentor.name AS "Local mentor"
FROM student LEFT JOIN mentor
ON student.mentor_id = mentor.id 
LEFT JOIN mentor AS "loc_mentor"
ON student.local_mentor = loc_mentor.id
ORDER BY student.name;*/

-- Task 2


/*SELECT student.name AS "Student",
module.name AS "Topic",
mentor.name AS "Mentor"
FROM student LEFT JOIN mentor
ON student.mentor_id = mentor.id 
LEFT JOIN module
ON module.teacher = mentor.id
ORDER BY student.name, module.name;*/


-- Task 3


/*SELECT module.name AS "Topic",
mentor.name AS "Mentor",
student.name AS "Student"
FROM student RIGHT JOIN mentor
ON student.mentor_id = mentor.id 
RIGHT JOIN module
ON module.teacher = mentor.id
ORDER BY module.name, student.name;*/


-- Task 4


/*SELECT module.name AS "Topic",
mentor.name AS "Mentor",
student.name AS "Student"
FROM student RIGHT JOIN mentor
ON student.mentor_id = mentor.id 
RIGHT JOIN module
ON module.teacher = mentor.id
WHERE student.city = 'Berlin' OR mentor.city = 'Berlin'
ORDER BY module.name, student.name*/;


-- Task Test


SELECT module.name AS "Topic",
mentor.name AS "Mentor",
student.name AS "Student"
FROM module LEFT JOIN mentor
ON module.teacher = mentor.id 
LEFT JOIN student
ON module.teacher = student.mentor_id
WHERE student.city = 'Berlin' OR mentor.city = 'Berlin'
ORDER BY module.name, student.name;
