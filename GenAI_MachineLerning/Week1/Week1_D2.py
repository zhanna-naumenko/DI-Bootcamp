import random

# Exercise 1: Favorite Numbers
my_fav_numbers = {10, 12, 11, 8}
my_fav_numbers.add(2)
my_fav_numbers.add(3)
print(my_fav_numbers)
my_fav_numbers.pop()
print(my_fav_numbers)

friend_fav_numbers = {1, 5 ,6}
our_fav_numbers = my_fav_numbers.union(friend_fav_numbers)
print(our_fav_numbers)

# Exercise 2: Tuple
my_tuple = (1, 2, 3)
add_tuple = (5,)
my_tuple += add_tuple
print(my_tuple)

# Exercise 3: List Manipulation
basket = ["Banana", "Apples", "Oranges", "Blueberries"]
print(basket)
basket.remove("Banana")
print(basket)
basket.remove("Blueberries")
print(basket)
basket.append("Kiwi")
print(basket)
basket.insert(1, "Apples")
print(basket)
basket.clear()
print(basket)

# Exercise 4: Floats
# Recap: What is a float? What’s the difference between a float and an integer?
# Integer is a whole number and float is the number with decimals
# Create a list containing the following sequence of mixed types: floats and integers:
# 1.5, 2, 2.5, 3, 3.5, 4, 4.5, 5.
mix_list = [1.5, 2, 2.5, 3, 3.5, 4, 4.5, 5]
# Avoid hard-coding each number manually.

# Think: Can you generate this sequence using a loop or another method?
mix_list2 = []
first = 1.5
while first <= 5:
    mix_list2.append(first)
    first += 0.5

print(mix_list2)

# Exercise 5: For Loop
# Write a for loop to print all numbers from 1 to 20, inclusive.
for val in range(1, 21):
    print(val)

# Write another for loop that prints every number from 1 to 20 where the index is even.

for i in range(1, 21):
    if i % 2 == 0:
        print(i)

# Exercise 6: While Loop

while True:
    user_name = input("Enter your name: ")
    if user_name.isalpha() and len(user_name) < 3:
        print("Your name is too short.\n")
    elif user_name.isdigit():
        print("Give the correct name.\n")
    else:
        break
print("Thank you")

# Exercise 7: Favorite Fruits
user_fruits = input("Please enter your favorite fruits separated by spaces: ").lower()
list_of_fruits = list(user_fruits.split(" "))
print(list_of_fruits)

today_fruit = input("Please enter what fruit are you eating right now: ").lower()

if today_fruit in list_of_fruits:
    print("You chose one of your favorite fruits! Enjoy!")
else:
    print("You chose a new fruit. I hope you enjoy it!")

# Exercise 8: Pizza Toppings
toppings = []
base_price = 10
topping_price = 2.5

while True:
    user_topping = input("Please enter what topping you want to add to the pizza. Enter 'quit' to stop: ").lower()

    if user_topping == "quit":
        break

    toppings.append(user_topping)
    print(f"Adding {user_topping} to your pizza.")

total_price = base_price + len(toppings)*topping_price

print("Your topics are:")
for topping in toppings:
    print(f"- {topping}")

print(f"Your total price for the pizza: ${total_price}")

# Exercise 9: Cinemax Tickets

child_ticket_price = 10
adult_ticket_price = 15

is_adult_movie = ["yes", "no"]
movie_pick_up = random.choice(is_adult_movie)
print(movie_pick_up)
list_of_attendees = []

while True:
    person_age = input("Enter your age. Enter 'quit' quit: ")
    if person_age.lower() == "quit":
        break
    if movie_pick_up == "yes":
        if 16 <= int(person_age) <= 21:
            list_of_attendees.append(int(person_age))
        else:
            print("Sorry, you are not allowed to watch this movie.")
    else:
        list_of_attendees.append(int(person_age))
total_price = 0
for num in list_of_attendees:
    if num < 3:
        total_price += 0
    elif 3 <= num <= 12:
        total_price += child_ticket_price
    else:
        total_price += adult_ticket_price
if movie_pick_up == "yes":
    print("The movie has restrictions. Only for ages 16-21")
else:
    print("The movie doesn't have restrictions. Everybody can watch it.")

print(f"Final attendees: {list_of_attendees}", )
print(f"The total price is: ${total_price}")

