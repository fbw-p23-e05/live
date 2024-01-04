# Task 1
CREATE DATABASE vehicles;

CREATE TABLE car_model(name VARCHAR(20), make VARCHAR(20),
year_of_checkin VARCHAR(4), engine_type VARCHAR(30), stock INT);

ALTER TABLE car_model ADD COLUMN engine_power VARCHAR(20);

\i /.../.../..path/vehicles.sql

# Task 2
\c postgres (or any other database)

DROP DATABASE vehicles;


# Task 3

ALTER TABLE car_model ADD COLUMN number_of_doors INT;

# Task 4
ALTER TABLE car_model RENAME COLUMN year_of_checkin TO year_of_manufacture;

# Task 5
ALTER TABLE car_model ALTER COLUMN year_of_manufacture TYPE INT
USING year_of_manufacture::integer;

# Task 6
ALTER TABLE car_model DROP COLUMN year_of_manufacture;