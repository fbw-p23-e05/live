-- Inserting data into vendors
INSERT INTO vendors(
	vendor_name,
	industry
)
VALUES ('RG Manufacturing', 'Manufacturing'),
		('PK Pharmaceuticals', 'Pharmaceutical'),
		('X Motors', 'Vehicles');
	
-- Insert data into the products table
INSERT INTO products(
	product_name,
	description,
	vendor_id
)
VALUES ('Paracetamol', 'Painkiller', 2),
		('CyberTruck', 'Electric flatbed truck', 3),
		('Steel rods', 'Steel for building use.', 1);

-- Insert data into the customers table
INSERT INTO customers(
	customer_name,
	industry
)
VALUES ('Blue Cat Inc.', 'Transportation');
