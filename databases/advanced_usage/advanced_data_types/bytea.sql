ALTER TABLE clients
ADD COLUMN client_img bytea;

SELECT 'hello 👋'::bytea::text;

INSERT INTO clients(
	client_name,
	phone_number,
	preferences, 
	client_img
)
VALUES ('John Johnson', '+3689797256454',
		'{"sculptures": "New Age", "paintings": "Old Age"}',
		'\x68656c6c6f20f09f918b');

SELECT * FROM clients
WHERE client_img = 'hello 👋';



