-- Exercise 1
-- 1.1 All items, ordered by price (lowest to highest)

-- SELECT * FROM items
-- ORDER BY item_price

-- 1.2 Items with a price above 80 (80 included), ordered by price (highest to lowest)

-- SELECT * FROM items
-- WHERE item_price >= 80
-- ORDER BY item_price DESC


-- 1.3 The first 3 customers in alphabetical order of the first name (A-Z) – exclude the primary key column from the results.

-- SELECT customer_first_name, customer_last_name FROM customer
-- ORDER BY customer_first_name ASC

-- 1.4 All last names (no other columns!), in reverse alphabetical order (Z-A)

-- SELECT customer_last_name FROM customer
-- ORDER BY customer_last_name DESC