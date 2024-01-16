-- Create a table contacts in friends DB
CREATE TABLE friends.contacts(
first_name VARCHAR(100),
last_name VARCHAR(100),
email_address VARCHAR(50),
phone_number VARCHAR(15)
);



-- inserting data into table contacts
-- INSERT INTO <table_name>(<column1>, <column2>...<columnN>) VALUES (<value1>, <value2>...<valueN>)
INSERT INTO contacts(first_name, last_name, email_address, phone_number)
VALUES ('John', 'Doe', 'johndoe.com', '+255785689254')

INSERT INTO contacts(first_name, last_name, email_address, phone_number)
VALUES ('Jane', 'Doe', 'janendoe.com', '+255487189254')

INSERT INTO contacts(first_name, last_name, email_address, phone_number)
VALUES ('Mark', 'Smith', 'Msmith.com', '+251234569254');



-- better this way :
-- inserting data into table contacts
-- INSERT INTO <table_name>(<column1>, <column2>...<columnN>) VALUES (<value1>, <value2>...<valueN>)
INSERT INTO contacts(first_name, last_name, email_address, phone_number)
VALUES ('John', 'Doe', 'johndoe.com', '+255785689254'),
	   ('Jane', 'Doe', 'janendoe.com', '+255487189254'), 
	   ('Mark', 'Smith', 'Msmith.com', '+251234569254');
	   
	  
-- retrieve some data from the database
-- SELECT <column1>, <column2>...<columnN> FROM <table_name>
SELECT first_name, phone_number FROM contacts;


-- retrieve all data from the table
-- SELECT * FROM <table_name>
SELECT * FROM contacts;


-- retrieve specific data from the table with all columns
-- SELECT * FROM <table_name> WHERE <column_name> = '<value>';
SELECT * FROM contacts WHERE last_name = 'Doe';


-- Updating data in a table:
-- UPDATE <table_name> SET <column1> = <value>, <column2> = value;
UPDATE contacts
SET email_address = 'common@email.com';


-- Updating data in a table:
-- UPDATE <table_name> SET <column1> = <value>, <column2> = value WHERE <column_name> = <value>;
UPDATE contacts
SET email_address = 'marksmith@rmail.com'
WHERE first_name = 'Mark';


-- delete some data from the contacts table
-- DELETE FROM <table_name> WHERE condtion 
DELETE FROM contacts
WHERE first_name = 'Jane' AND email_address = 'common@email.com';

-- delete a table from a database
-- DROP TABLE <table_name>;
DROP TABLE contacts;


