-- Database: Hollywood

-- DROP DATABASE IF EXISTS "Hollywood";

-- CREATE DATABASE "Hollywood"
--     WITH
--     OWNER = postgres
--     ENCODING = 'UTF8'
--     LC_COLLATE = 'Russian_Russia.1251'
--     LC_CTYPE = 'Russian_Russia.1251'
--     LOCALE_PROVIDER = 'libc'
--     TABLESPACE = pg_default
--     CONNECTION LIMIT = -1
--     IS_TEMPLATE = False;

-- SELECT * FROM actors
-- ORDER BY actor_id asc

-- 1.Count how many actors are in the table.
-- SELECT COUNT(*) FROM actors

-- 2.Try to add a new actor with some blank fields
-- INSERT INTO actors (first_name, last_name, oscars, birthday)
-- VALUES ('', '', 0, '')
-- it will be an ERROR
