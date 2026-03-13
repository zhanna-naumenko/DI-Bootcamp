-- Part 1
-- 1.Create 2 tables : Customer and Customer profile

-- CREATE TABLE customer (
-- id SERIAL PRIMARY KEY,
-- first_name VARCHAR (50) NOT NULL,
-- last_name VARCHAR (100) NOT NULL)

-- CREATE TABLE customer_profile(
-- id SERIAL PRIMARY KEY,
-- isLoggedIn Boolean DEFAULT false,
-- customer_id INT NOT NULL,
-- CONSTRAINT fk_customer_id FOREIGN KEY (customer_id) REFERENCES customer(id))

-- INSERT INTO customer(first_name, last_name)
-- VALUES ('John', 'Doe'), ('Jerome', 'Lalu'), ('Lea', 'Rive')

-- INSERT INTO customer_profile (isLoggedIn, customer_id)
-- VALUES (true, (SELECT id FROM customer WHERE first_name = 'John')),
-- (false, (SELECT id FROM customer WHERE first_name = 'Jerome'))


-- SELECT customer.first_name FROM customer
-- INNER JOIN customer_profile
-- ON customer_profile.customer_id = customer.id
-- WHERE customer_profile.isLoggedIn = true

-- SELECT customer.first_name, COALESCE(customer_profile.isLoggedIn, false) AS isLoggedIn FROM customer
-- LEFT JOIN customer_profile
-- ON customer_profile.customer_id = customer.id

-- SELECT COUNT (*) AS not_loggedIn FROM customer
-- WHERE id NOT IN (SELECT customer_id FROM customer_profile WHERE customer_profile.isLoggedIn = true)

-- Part 2

-- CREATE TABLE book (
-- book_id SERIAL PRIMARY KEY,
-- title VARCHAR (100) NOT NULL,
-- author VARCHAR (50) NOT NULL)

-- INSERT INTO book (title, author)
-- VALUES ('Alice In Wonderland', 'Lewis Carroll'), ('Harry Potter', 'J.K Rowling'), ('To kill a mockingbird', 'Harper Lee')

-- CREATE TABLE student (
-- student_id SERIAL PRIMARY KEY,
-- name VARCHAR (50) NOT NULL UNIQUE,
-- age SMALLINT NOT NULL
-- CONSTRAINT age_val CHECK (age <= 15))

-- INSERT INTO student(name, age)
-- VALUES ('John', 12), ('Lera', 11), ('Patrick', 10), ('Bob', 14)

-- CREATE TABLE library (
-- book_fk_id INT,
-- student_id INT,
-- borrowed_date DATE,
-- PRIMARY KEY (book_fk_id, student_id),
-- FOREIGN KEY (book_fk_id) REFERENCES book(book_id) ON DELETE CASCADE ON UPDATE CASCADE,
-- FOREIGN KEY (student_id) REFERENCES student(student_id) ON DELETE CASCADE ON UPDATE CASCADE
-- )

-- INSERT INTO library (book_fk_id, student_id, borrowed_date)
-- VALUES ((SELECT book_id FROM book WHERE title = 'Alice In Wonderland'), (SELECT student_id FROM student WHERE name = 'John'), '2022-02-15'),
-- ((SELECT book_id FROM book WHERE title = 'To kill a mockingbird'), (SELECT student_id FROM student WHERE name = 'Bob'), '2021-03-03'),
-- ((SELECT book_id FROM book WHERE title = 'Alice In Wonderland'), (SELECT student_id FROM student WHERE name = 'Lera'), '2021-05-23'),
-- ((SELECT book_id FROM book WHERE title = 'Harry Potter'), (SELECT student_id FROM student WHERE name = 'Bob'), '2021-08-12')

-- SELECT * FROM library

-- SELECT student.name, book.title FROM student
-- JOIN library
-- ON student.student_id = library.student_id
-- JOIN book
-- ON library.book_fk_id = book.book_id


-- SELECT AVG(student.age) AS average_age
-- FROM student
-- JOIN library
-- ON student.student_id = library.student_id
-- JOIN book
-- ON library.book_fk_id = book.book_id
-- WHERE book.title = 'Alice In Wonderland'

-- DELETE FROM student WHERE name = 'Patrick'
