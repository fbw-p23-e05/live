-- Task 4

-- 1.

SELECT * FROM site_user
WHERE birthdate < '2000-01-01';

-- 2.

SELECT * FROM site_user
WHERE siblings IS NOT NULL;

SELECT * FROM site_user
WHERE array_length(siblings, 1) > 0;

-- 3.

SELECT * FROM site_user
WHERE site_settings ->> 'notifications' = 'true';

-- 4.

SELECT * FROM site_user
WHERE array_length(availability, 1) > 1;