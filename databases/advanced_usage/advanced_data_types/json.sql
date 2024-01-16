CREATE TABLE clients(
	client_id uuid DEFAULT uuid_generate_v4(),
	client_name VARCHAR(100),
	phone_number VARCHAR(50),
	preferences json,
	PRIMARY KEY(client_id)
);

INSERT INTO clients(
	client_name,
	phone_number,
	preferences
)
VALUES ('John Whitherspoon', '+356558945177',
		'{"sculptures": "Old Age", "paintings": "Realism"}');

SELECT preferences -> 'paintings' FROM clients;

SELECT preferences ->> 'sculptures', preferences ->> 'paintings' FROM clients;
