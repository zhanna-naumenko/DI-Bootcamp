import random

# Exercise 1: What Are You Learning?
def display_message():
    print("I am learning about functions in Python.")

display_message()

# Exercise 2: What’s Your Favorite Book?
def favorite_book(title):
    print(f"One of my favorite books is {title}.")

favorite_book("The Lord Of The Rings")

# Exercise 3: Some Geography
def describe_city(city, country = "Unknown"):
    print(f"{city} is in {country}.")

describe_city("Mumbai", "India")
describe_city("Odessa", "Ukraine")
describe_city("Whatever")

# Exercise 4: Random
def guess_random_number(num):
    if not 1 <= num <= 100:
        print("Please provide a number between 1 and 100.")
        return
    random_number = random.randint(1, 101)
    if num == random_number:
        print("Success!")
    else:
        print(f"Fail! Your number: {num}, Random number: {random_number}")

guess_random_number(50)
guess_random_number(10)
guess_random_number(101)

# Exercise 5: Let’s Create Some Personalized Shirts!
def make_shirt(size = "large", text = "I love Python"):
    print(f"The size of the shirt is  {size} and the text is  {text}.")

make_shirt()
make_shirt("medium")
make_shirt("small", "I want to eat")

# Exercise 6: Magicians
magician_names = ["Harry Houdini", "David Blaine", "Criss Angel", "Harry Potter"]

def show_magicians(lst):
    for magician in lst:
        print(f"Magician - {magician}")

def make_great(lst):
    for magician in lst:
        print(f"{magician} the Great")

show_magicians(magician_names)
make_great(magician_names)

# Exercise 7: Temperature Advice
def get_random_temp():
    return round(random.uniform(-10, 40), 1)

def main():
    today_degree = get_random_temp()
    print(f"The temperature right now is {today_degree} degrees Celsius.")
    if today_degree < 0:
        print("Brrr, that’s freezing! Wear some extra layers today.")
    elif 0 < today_degree < 16:
        print("Quite chilly! Don’t forget your coat.")
    elif 16 <= today_degree <= 23:
        print("Nice weather.")
    elif 24 <= today_degree <= 32:
        print("A bit warm, stay hydrated.")
    elif 32 < today_degree <= 40:
        print("It’s really hot! Stay cool.")

main()

