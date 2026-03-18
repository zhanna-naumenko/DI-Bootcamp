-- Database: bootcamp

-- DROP DATABASE IF EXISTS bootcamp;

-- 1. CREATE DATABASE bootcamp
--     WITH
--     OWNER = postgres
--     ENCODING = 'UTF8'
--     LC_COLLATE = 'Russian_Russia.1251'
--     LC_CTYPE = 'Russian_Russia.1251'
--     LOCALE_PROVIDER = 'libc'
--     TABLESPACE = pg_default
--     CONNECTION LIMIT = -1
--     IS_TEMPLATE = False;

-- 2.Create a table called students

-- CREATE TABLE students(
-- student_id SERIAL PRIMARY KEY,
-- last_name VARCHAR (50) NOT NULL,
-- first_name VARCHAR (100) NOT NULL,
-- birth_date DATE NOT NULL
-- )

-- 3.Insert the data and my last_name, first_name and birth_date to the students table

-- INSERT INTO students(last_name, first_name, birth_date)
-- VALUES ('Benichou', 'Marc', '02/11/1998'), ('Cohen', 'Yoan', '03/12/2010'), ('Benichou', 'Lea', '27/07/1987'), ('Dux', 'Amelia', '07/04/1996'), ('Grez', 'David', '14/06/2003'), ('Simpson', 'Omer', '03/10/1980'),('Naumenko', 'Zhanna', '03/08/1988')  

-- 4.Fetch all of the data from the table.
-- SELECT * FROM students

-- 5.Fetch all of the students first_names and last_names.
-- SELECT last_name, first_name FROM students

-- 6.For the following questions, only fetch the first_names and last_names of the students:
-- 6.1. Fetch the student which id is equal to 2
-- SELECT last_name, first_name FROM students
-- WHERE student_id = 2

-- 6.2. Fetch the student whose last_name is Benichou AND first_name is Marc
-- SELECT last_name, first_name FROM students
-- WHERE last_name = 'Benichou' AND first_name = 'Marc'

-- 6.3.Fetch the students whose last_names are Benichou OR first_names are Marc.
-- SELECT last_name, first_name FROM students
-- WHERE last_name = 'Benichou' OR first_name = 'Marc'

-- 6.4.Fetch the students whose first_names contain the letter a
-- SELECT last_name, first_name FROM students
-- WHERE first_name LIKE '%a%'

-- 6.5.Fetch the students whose first_names start with the letter a
-- SELECT last_name, first_name FROM students
-- WHERE first_name ILIKE 'a%'

-- 6.6. Fetch the students whose first_names end with the letter a
-- SELECT last_name, first_name FROM students
-- WHERE first_name ILIKE '%a'

-- 6.7.Fetch the students whose second to last letter of their first_names are a
-- SELECT last_name, first_name FROM students
-- WHERE first_name LIKE '%a_'

-- 6.8.Fetch the students whose id’s are equal to 1 AND 3
-- SELECT last_name, first_name FROM students
-- WHERE student_id = 1 OR student_id = 3

-- 7.Fetch the students whose birth_dates are equal to or come after 1/01/2000
-- SELECT * FROM students
-- WHERE birth_date >= '01/01/2000'
