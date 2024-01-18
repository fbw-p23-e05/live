UPDATE clients 
SET phone_number = '+245898523458987'
WHERE client_id IN (
	SELECT client_id FROM clients 
	WHERE client_name = 'John Whitherspoon'
);