-- Exercise 1
-- 1.Get a list of all the languages, from the language table
-- SELECT DISTINCT name FROM language

-- 2.Get a list of all films joined with their languages – select the following details : 
-- film title, description, and language name.

-- SELECT film.title, film.description, language.name FROM film
-- INNER JOIN language
-- ON film.language_id = language.language_id

-- 3.Get all languages, even if there are no films in those languages – select 
-- the following details : film title, description, and language name.

-- SELECT language.name, film.title, film.description FROM film
-- RIGHT JOIN language
-- ON film.language_id = language.language_id

-- 4.Create a new table called new_film with the following columns : id, name. Add some new films to the table
-- CREATE TABLE new_film(
-- id SERIAL PRIMARY KEY,
-- name VARCHAR (100) NOT NULL)

-- INSERT INTO new_film(name)
-- VALUES ('The fifth element'), ('The lord of the rings'), ('The Hobbit'), ('Equilibrium'), ('The black hole')

-- 5.Create a new table called customer_review
-- CREATE TABLE customer_review(
-- review_id SERIAL PRIMARY KEY,
-- film_id INTEGER NOT NULL,
-- language_id INTEGER NOT NULL,
-- title VARCHAR (100) NOT NULL,
-- score SMALLINT NOT NULL,
-- review_text TEXT NOT NULL,
-- last_update DATE NOT NULL,
-- FOREIGN KEY (film_id) REFERENCES film(film_id) ON UPDATE CASCADE,
-- FOREIGN KEY (language_id) REFERENCES language(language_id) ON UPDATE CASCADE,
-- CONSTRAINT score_val CHECK (score > 0 AND score <= 10)
-- );


-- 6. Add 2 movie reviews.

-- INSERT INTO customer_review (film_id, language_id, title, score, review_text, last_update)
-- VALUES ((SELECT film_id FROM film where name = 'The fifth element'), (SELECT language_id FROM language where language_id = 1), 'Multi Pass', 8, 'This amazing sci-fi adventure from Luc (Leon) Besson has a little something for everyone. 
-- 		Beauty (the gorgeous Jovovich with orange hair even), action and gun-play, excellent acting, amazing visual effects, romance, creative sets and costume design, dynamic and interesting music and a mildly annoying but funny Chris Tucker. 
-- 		You name it this film has it in spades. 5th Element is hands down one of the best science fiction films ever.I have seen it many times and always want more. I highly recommended it.', '2005-01-23'),
-- 		((SELECT film_id FROM film where name = 'The lord of the rings'), (SELECT language_id FROM language where language_id = 1), 'First, And Still The Best Of LOTR', 10, 'The story covers all kinds of terrain, too, from the lush Shire of the Hobbits, to the harsh neighboring landscapes. 
-- 		 Each couple of minutes, as in the two movies that followed, scenes radically change from calmness to action, adventure to romance, sweet lovable characters to hideous monsters, on and on and on. It is an incredible movie experience', '2006-03-07')


-- 7.Delete a film that has a review from the new_film table
-- DELETE FROM new_film
-- WHERE id = 1

-- Exercise 2

-- 1.Use UPDATE to change the language of some films. Make sure that you use valid languages.
-- UPDATE film
-- SET language_id = 2
-- WHERE film_id = 1
-- UPDATE film
-- SET language_id = 3
-- WHERE film_id = 2
-- UPDATE film
-- SET language_id = 2
-- WHERE film_id = 3


-- 2.Which foreign keys (references) are defined for the customer table? 
-- How does this affect the way in which we INSERT into the customer table?
-- There is customer_id in rental table and customer_id in payment as a foreign key.
-- When foreign keys are defined for a table we need to ensure that the data being 
-- inserted adheres to the referential integrity rules defined by those constraints.

-- 3.We created a new table called customer_review. Drop this table. 
-- DROP TABLE customer_review

-- 4.Find out how many rentals are still outstanding (ie. have not been returned to the store yet).
-- SELECT * FROM rental
-- WHERE (return_date is NULL)

-- 5.Find the 30 most expensive movies which are outstanding (ie. have not been returned to the store yet)
-- SELECT * FROM rental
-- INNER JOIN inventory
-- ON rental.inventory_id = inventory.inventory_id
-- INNER JOIN film
-- ON inventory.film_id = film.film_id
-- WHERE rental.return_date IS NULL
-- ORDER BY film.replacement_cost DESC LIMIT 30

-- 6.1.The 1st film : The film is about a sumo wrestler, and one of the actors is Penelope Monroe.
-- SELECT CONCAT (actor.first_name, ' ', actor.last_name), film.title FROM actor
-- INNER JOIN film_actor
-- ON film_actor.actor_id = actor.actor_id
-- INNER JOIN film
-- ON film_actor.film_id = film.film_id
-- WHERE actor.first_name = 'Penelope' AND actor.last_name = 'Monroe' AND film.description ILIKE '%sumo wrestler%'

-- 6.2. The 2nd film : A short documentary (less than 1 hour long), rated “R”.

-- SELECT * FROM film
-- WHERE description like '%Documentary%' AND length < 60 AND rating = 'R'

-- 6.3.The 3rd film : A film that his friend Matthew Mahan rented. 
-- He paid over $4.00 for the rental, 
-- and he returned it between the 28th of July and the 1st of August, 2005

-- SELECT CONCAT (customer.first_name,' ', customer.last_name), film.title, payment.amount FROM customer
-- INNER JOIN payment
-- ON customer.customer_id = payment.customer_id
-- INNER JOIN rental
-- ON payment.rental_id = rental.rental_id
-- INNER JOIN inventory
-- ON rental.inventory_id = inventory.inventory_id
-- INNER JOIN film
-- ON inventory.film_id = film.film_id
-- WHERE customer.first_name = 'Matthew' AND customer.last_name = 'Mahan' 
-- AND payment.amount = 4.99 AND rental.return_date BETWEEN '2005-07-28' AND '2005-08-01'

-- 6.4.The 4th film : His friend Matthew Mahan watched this film, as well. 
-- It had the word “boat” in the title or description, and it looked like it was a very expensive DVD to replace.


-- SELECT CONCAT (customer.first_name, ' ', customer.last_name), film.title, film.replacement_cost FROM customer
-- INNER JOIN payment
-- ON customer.customer_id = payment.customer_id
-- INNER JOIN rental
-- ON payment.rental_id = rental.rental_id
-- INNER JOIN inventory
-- ON rental.inventory_id = inventory.inventory_id
-- INNER JOIN film
-- ON inventory.film_id = film.film_id
-- WHERE customer.first_name = 'Matthew' AND customer.last_name = 'Mahan' 
-- AND (film.title ILIKE '%boat%' OR film.description ILIKE '%boat%')
-- ORDER BY film.replacement_cost DESC LIMIT 1