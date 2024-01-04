DROP DATABASE IF EXISTS vehicles;

CREATE DATABASE vehicles;

\c vehicles

CREATE TABLE car_model(name VARCHAR(20), make VARCHAR(20),
year_of_checkin VARCHAR(4), engine_type VARCHAR(30), stock INT);

ALTER TABLE car_model ADD COLUMN engine_power VARCHAR(20);
