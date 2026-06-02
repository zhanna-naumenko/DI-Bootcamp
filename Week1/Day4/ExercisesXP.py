import random


# Exercise 1
def display_message():
    '''Prints the message'''
    print("I'm learning Data Analise, Python, Databases and many other cool stuff.")


display_message()


# Exercise 2
def favorite_book(title):
    '''Takes the parameter title and print out the message'''
    print(f"One of my favorite books is {title}")


favorite_book("The Lord of the Ring")


# Exercise 3
def describe_city(city, country):
    '''Takes two parameters the city and the country and print out the message'''
    print(f"{city} is in {country}")


describe_city(country="Canada", city="Vancouver")
describe_city('Odessa', 'Ukraine')

#Exercise 4
def number_generator(num):
    '''Takes the parameter number, generates a random number and if numbers are
    equal displays a success message, otherwise show a fail message and display both numbers. '''
    if num > 100 or num <= 0:
        print("The number should be from 1 to 100.")
    else:
        num2 = random.randint(1, 100)
        if num == num2:
            print("Success! Congratulations, you guessed the correct number!")
        else:
            print(f"You failed!\nYour number is: {num}.\nThe random number is: {num2}.")


user_input = int(input("Please enter a number between 1 and 100: "))
number_generator(user_input)

#Exercise 5
list_of_sizes = ["XS", "S", "M", "L", "XL", "XXL", "XXXL"]
def make_shirt(size, message):
    if size.upper() in list_of_sizes:
        print(f"The size of the shirt is {size} and the text is {message}")
    else:
        print(f"Your size is not exist. Please choose from the list {', '.join(list_of_sizes)}")

user_size = input("Please enter the size of your shirt: ")
user_message = input("Please enter the message you want to print on your shirt: ")
make_shirt(size=user_size, message=user_message)

#Exercise 6
magician_names = ['Harry Houdini', 'David Blaine', 'Criss Angel']

def show_magicians(magicians):
    '''Prints the name of each magician that are in the list magician_names'''
    for magician in magicians:
        print(magician)

def make_great(magicians):
    """Modifies the original list of magicians by adding the phrase "the Great"."""
    for magician in range(len(magicians)):
        magicians[magician] = "the Great" + " " + magicians[magician]

print("Original Magician Names:")
show_magicians(magician_names)
make_great(magician_names)
print("\nModified Magician Names:")
show_magicians(magician_names)

#Exercise 7
def get_random_temp(season):
    """Returns a random temperature based on the specified season."""
    if season.lower() == "winter":
        return random.randint(-10, 16)
    elif season.lower() == 'spring' or season.lower() == 'autumn' or season.lower() == 'fall':
        return random.randint(0, 23)
    elif season.lower() == 'summer':
        return random.randint(24, 40)
    else:
        print("Invalid season. Using default temperature range (-10 to 40).")
        return random.randint(-10, 40)


friendly_advice = {0: "Brrr, that’s freezing! Wear some extra layers today",
                   16: "Quite chilly! Don’t forget your coat.",
                   23: "It's a good temperature, but take a sweater.",
                   32: "It's hot!",
                   40: "Be careful! It's extremely hot!"}
def main():
    season = input("Enter the season (summer, autumn, winter, spring): ")
    today_temp = get_random_temp(season)
    print(f"The temperature right now is {today_temp} degrees Celsius.")
    for temperature, advice in friendly_advice.items():
        if today_temp <= temperature:
            return advice

print(main())
print(get_random_temp("winter"))

#Exercise 8
data = [
    {
        "question": "What is Baby Yoda's real name?",
        "answer": "Grogu"
    },
    {
        "question": "Where did Obi-Wan take Luke after his birth?",
        "answer": "Tatooine"
    },
    {
        "question": "What year did the first Star Wars movie come out?",
        "answer": "1977"
    },
    {
        "question": "Who built C-3PO?",
        "answer": "Anakin Skywalker"
    },
    {
        "question": "Anakin Skywalker grew up to be who?",
        "answer": "Darth Vader"
    },
    {
        "question": "What species is Chewbacca?",
        "answer": "Wookiee"
    }
]

def ask_questions(questions):
    """Asks the user the questions and checks the answers."""
    correct_answers = 0
    incorrect_answers = 0
    wrong_answers = []

    for question_data in questions:
        question = question_data["question"]
        correct_answer = question_data["answer"]

        user_answer = input(f"{question}\nYour Answer: ").strip()

        if user_answer.lower() == correct_answer.lower():
            print("Correct!\n")
            correct_answers += 1
        else:
            print(f"Incorrect. The correct answer is: {correct_answer}\n")
            incorrect_answers += 1
            wrong_answers.append({"question": question, "user_answer": user_answer, "correct_answer": correct_answer})

    return correct_answers, incorrect_answers, wrong_answers

def display_results(correct, incorrect, wrong_answers):
    """Informs the user of their number of correct/incorrect answers and provides a list of wrong answers."""
    print(f"\nResults:")
    print(f"Correct Answers: {correct}")
    print(f"Incorrect Answers: {incorrect}")

    if incorrect > 0:
        print("\nList of Wrong Answers:")
        for wrong_answer in wrong_answers:
            print(f"Question: {wrong_answer['question']}")
            print(f"Your Answer: {wrong_answer['user_answer']}")
            print(f"Correct Answer: {wrong_answer['correct_answer']}\n")

correct_count, incorrect_count, wrong_answers_list = ask_questions(data)
display_results(correct_count, incorrect_count, wrong_answers_list)

