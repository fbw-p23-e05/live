-- Vendors table
CREATE TABLE vendors(
	vendor_id SERIAL PRIMARY KEY,
	vendor_name VARCHAR(200) NOT NULL,
	industry VARCHAR(100)
);

-- Products table
CREATE TABLE products(
	product_id SERIAL PRIMARY KEY,
	product_name VARCHAR(100) NOT NULL,
	description TEXT,
	vendor_id INT,
	FOREIGN KEY (vendor_id)
		REFERENCES vendors(vendor_id)
		ON UPDATE CASCADE ON DELETE CASCADE
);

-- Customers table
CREATE TABLE customers(
	customer_id SERIAL PRIMARY KEY,
	customer_name VARCHAR(200) NOT NULL,
	industry VARCHAR
);