-- Database: bootcamp

-- DROP DATABASE IF EXISTS bootcamp;

-- CREATE DATABASE bootcamp
--     WITH
--     OWNER = postgres
--     ENCODING = 'UTF8'
--     LC_COLLATE = 'Russian_Russia.1251'
--     LC_CTYPE = 'Russian_Russia.1251'
--     LOCALE_PROVIDER = 'libc'
--     TABLESPACE = pg_default
--     CONNECTION LIMIT = -1
--     IS_TEMPLATE = False;

-- 1.Fetch the first four students. You have to order the four students alphabetically by last_name.
-- SELECT first_name, last_name, birth_date FROM students 
-- ORDER BY last_name asc LIMIT 4

-- 2.Fetch the details of the youngest student
-- SELECT first_name, last_name, birth_date FROM students
-- ORDER BY birth_date DESC LIMIT 1

-- 3.Fetch three students skipping the first two students.
-- SELECT first_name, last_name, birth_date FROM students OFFSET 2 LIMIT 3
