-- -- Database: public

-- -- DROP DATABASE IF EXISTS public;

-- 1. CREATE DATABASE public
--     WITH
--     OWNER = postgres
--     ENCODING = 'UTF8'
--     LC_COLLATE = 'Russian_Russia.1251'
--     LC_CTYPE = 'Russian_Russia.1251'
--     LOCALE_PROVIDER = 'libc'
--     TABLESPACE = pg_default
--     CONNECTION LIMIT = -1
--     IS_TEMPLATE = False;

-- 2. creating a table items and customers

-- CREATE TABLE items(
-- item_id SERIAL PRIMARY KEY,
-- item_name VARCHAR (50) NOT NULL,
-- item_price INTEGER NOT NULL
-- )

-- CREATE TABLE customer(
-- customer_id SERIAL PRIMARY KEY,
-- customer_first_name VARCHAR (50) NOT NULL,
-- customer_last_name VARCHAR (100) NOT NULL
-- )

-- Add the items to the items table

-- INSERT INTO items (item_name, item_price)
-- VALUES ('Small Desk', 100), ('Large desk', 300), ('Fan', 80)

-- INSERT INTO customer (customer_first_name, customer_last_name)
-- VALUES ('Greg', 'Jones'), ('Sandra', 'Jones'), ('Scott', 'Scott'), ('Trevor', 'Green'), ('Melanie', 'Johnson')

-- 3.Use SQL to fetch the following data from the database

-- 1.All the items
-- SELECT * FROM items
-- SELECT * FROM customer

-- 2.All the items with a price above 80 (80 not included).
-- SELECT * FROM items
-- WHERE item_price > 80

-- 3.All the items with a price below 300. (300 included)
-- SELECT * FROM items
-- WHERE item_price <= 300

-- 4.All customers whose last name is ‘Smith’.

-- SELECT * FROM customer
-- WHERE customer_last_name = 'Smith'

-- 5.All customers whose last name is ‘Jones’

-- SELECT * FROM customer
-- WHERE customer_last_name = 'Jones'

-- 6.All customers whose firstname is not ‘Scott’

-- SELECT * FROM customer
-- WHERE customer_last_name != 'Scott'




