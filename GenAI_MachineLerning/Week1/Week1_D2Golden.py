import string
import time
import random

# Exercise 1: Concatenate lists
# Write code that concatenates two lists together without using the + sign.
list1 = [1, 2, 3]
list2 = [5, 3, 9]
list1.extend(list2)
print(list1)

# Exercise 2: Range of numbers
# Create a loop that goes from 1500 to 2500 and prints all multiples of 5 and 7.
for num in range(1500, 2501):
    if num % 5 == 0 and num % 7 == 0:
        print(num)

# Exercise 3: Check the index
names = ['Samus', 'Cortana', 'V', 'Link', 'Mario', 'Cortana', 'Samus']

user_name = input("Please enter your name: ")

if user_name in names:
    print(f"The name {user_name} has {names.index(user_name)} index in the list.")
else:
    print("Your name not in the list.")

# Exercise 4: Greatest Number

user_numbers = []

for num in range(1, 4):
    user_number = int(input(f"Please enter the {num} number: "))
    user_numbers.append(user_number)

greatest_number = max(user_numbers)

print(f"The greatest number is: {greatest_number}")

# Exercise 5: The Alphabet
list_letters = list(string.ascii_lowercase)
list_vowels = ['a', 'e', 'i', 'o', 'u']
for letter in list_letters:
    if letter not in list_vowels:
        print(f"{letter} is consonant")
    else:
        print(f"{letter} is vowel")

# Exercise 6: Words and letters

number_words = 7
list_of_user_words = []
while number_words > 0:
    user_word = input("Please enter a word: ")
    list_of_user_words.append(user_word)
    number_words -= 1

print(list_of_user_words)

user_letter = input("Please enter your letter: ")

for item in list_of_user_words:
    if user_letter in item:
        print(f"The index of {user_letter} in word {item} is {item.index(user_letter)}")
    else:
        print(f"There is no letter {user_letter} in word {item}.")

# Exercise 7: Min, Max, Sum
time_start = time.time()
print(f"Start time: {time_start}`")
million_list = list(range(1,1000001))
end_time = time.time()
print(f"End time: {end_time}`")
print(f"There is need time to create a million list in sec: {end_time - time_start}")

# Checking the first and the last element in the list
print(million_list[0])
print(million_list[-1])
# Checking the max and min element in the list
print(min(million_list))
print(max(million_list))


# Exercise 8 : List and Tuple

user_numbers = input("Please enter sequence of comma-separated numbers: ")
list_numbers = list(user_numbers.split(","))
print(list_numbers)
set_numbers = tuple(list_numbers)
print(set_numbers)

# Exercise 9 : Random number

game_on = True
total_win = 0
total_lose = 0

while game_on:
    random_number = random.randint(1, 10)
    user_number = input("Please enter number. If you want to quit enter 'q': ")
    if user_number == "q":
        print("Good Bye!")
        break
    number = int(user_number)
    if number == random_number:
        print("You got it! Winner!")
        total_win += 1
        continue
    elif number != random_number:
        total_lose += 1
        print("Please enter different number.")

print(f"The total of wins: {total_win}, the total of loses: {total_lose}")
