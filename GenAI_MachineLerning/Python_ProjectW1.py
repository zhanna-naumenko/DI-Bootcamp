import random

print("Welcome to Number Guessing Game!\nYou need to guess the number between 1 and 100. You will have only 7 attempts.")

random_num = random.randint(1, 101)
numb_attempts = 0
while numb_attempts < 7:
    user_number = int(input("Enter a number: "))
    if user_number == random_num:
        print("You win! You guessed the number!")
        break
    elif user_number > random_num:
        print("The number is too high!")
        numb_attempts += 1
        print(f"You left {numb_attempts} attempts")
    elif user_number < random_num:
        print("The number is too low!")
        numb_attempts += 1
        print(f"You left {numb_attempts} attempts")

