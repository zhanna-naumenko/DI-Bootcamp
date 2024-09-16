import string
import time
import random

# Exercise 1
list1 = ["moon", "sun", "stars"]
list2 = ["people", "animals"]

list3 = [*list1, *list2]
print(list3)

# Exercise 2

for num in range(1500, 2501):
    if num % 5 == 0 or num % 7 == 0:
        print(num)

# Exercise 3

names = ['Samus', 'Cortana', 'V', 'Link', 'Mario', 'Cortana', 'Samus']

user_name = (input("Please write your name: ")).capitalize()

if user_name in names:
    print(f"Your name is in the list. The index: {names.index(user_name)}")
else:
    print("Your name is not in the list.")

# Exercise 4

number = 1
list_of_numbers = []

for number in range(1, 4):
    num = int(input(f"Please write {number} number: "))
    list_of_numbers.append(num)
    number += 1
print(f"The greatest number is: {max(list_of_numbers)}")


# Exercise 5
letters = string.ascii_lowercase

vowel_letters = ['a', 'e', 'i', 'o', 'u', 'y']

for letter in letters:
    if letter in vowel_letters:
        print(f"The letter {letter} is a vowel.")
    else:
        print(f"The letter {letter} is a consonant.")

# Exercise 6

user_words = input("Please write 7 words separating with comma: ")
words = list(user_words.split(" "))
print(words)
if len(words) == 7:
    letter = input("Please write a letter: ").lower()
    if letter in string.ascii_lowercase:
        for word in words:
            if letter in word:
                index_letter = word.index(letter) + 1
                print(f"The letter {letter} in word {word} in {index_letter} position.")
            else:
                print(f"The letter {letter} not in the word {word}")
    else:
        print("Please choose another letter.")
else:
    print("There is not 7 words. Please try again.")

# Exercise 7

list_of_numbers = list(range(1, 1000001))
print(min(list_of_numbers))
print(max(list_of_numbers))

start = time.time()
sum_of_numbers = 0
for num in list_of_numbers:
    sum_of_numbers += num
print(sum_of_numbers)
end = time.time()
print(end - start)

# Exercise 8

user_numbers = input("Please write a numbers separated ONLY by comma: ")

print(list(user_numbers.split(",")))
print(tuple(user_numbers.split(",")))


# Exercise 9

end_of_game = False
number_of_wins = 0
number_of_loose = 0

while not end_of_game:
    your_number = int(input("Please input a number from 1 to 9: "))
    random_number = random.randint(1, 9)

    if your_number <= 9 and your_number >= 1:
        if your_number == random_number:
            number_of_wins += 1
            print("Congratulations! You won!")
        else:
            number_of_loose += 1
            print("Please try again.")

        one_more_time = input("Do you want to try again? yes or no: ").lower()
        if one_more_time == "no":
            end_of_game = True
    else:
        print("Please enter a valid number between 1 and 9.")

print(f"Number of wins: {number_of_wins}")
print(f"Number of losses: {number_of_loose}")