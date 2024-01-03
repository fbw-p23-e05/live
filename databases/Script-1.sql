-- Creates a table called contacts in the friends DB

CREATE TABLE public.contacts(
first_name VARCHAR(100),
last_name VARCHAR(100),
email_address VARCHAR(50),
phone_number VARCHAR(15)
);

-- Inserting data into table contacts
-- INSERT INTO <table_name>(<column1>, <column2>...<columnN>) VALUES (<value1>, <value2>...<valueN>)
INSERT INTO contacts(first_name, last_name, email_address, phone_number)
VALUES ('John', 'Doe', 'john@doe.com', '+255785689254'), 
		('Jane', 'Doe', 'jane@doe.com', '+255798589254'), 
		('Mark', 'Smith', 'mark@yahoo.com', '+287962456125');
		

-- Retrieve some data from the database
-- SELECT <column1>, <column2>...<columnN> FROM <table_name>;
SELECT first_name, email_address FROM contacts;


-- Retrieve all columns from the table
-- SELECT * FROM <table_name>;
SELECT * FROM contacts;

-- Retrieve specific data from the table with all columns
-- SELECT * FROM <table_name> WHERE <column_name> = '<value>';
SELECT * FROM contacts WHERE last_name = 'Doe';

-- Updating data in a table
-- UPDATE <table_name> SET <column1> = <value>, <column2> = value;
UPDATE contacts
SET email_address = 'common@email.com';

-- Updating data in a table with a conditon
-- UPDATE <table_name> SET <column1> = <value>, <column2> = value WHERE <column_name> = '<value>';
UPDATE contacts
SET email_address = 'marksmith@email.com'
WHERE first_name = 'Mark';


-- Delete some dataa from the contacts table
-- DELETE FROM <table_name> WHERE condition;
DELETE  FROM contacts 
WHERE first_name = 'Jane' AND email_address = 'common@email.com';


-- Delete a table from a database
-- DROP TABLE <table_name>;
DROP TABLE contacts;


-- Delete database
-- DROP DATABASE <database name>
DROP DATABASE friends;



