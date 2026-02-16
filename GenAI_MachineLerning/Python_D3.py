import string
# Exercise 1 : Dictionary Exercises
# Instructions
# Write the following Python code to do the following (Complete ALL of the following using dictionary comprehension)
# 1.Given a list [("name", "Elie"), ("job", "Instructor")], create a dictionary that looks like this {'job': 'Instructor', 'name': 'Elie'} (the order does not matter).
from Python_D2 import vowels

user_list = [("name", "Elie"), ("job", "Instructor")]
user_dict = {}
for i in range(0, len(user_list)):
    for key, value in user_list:
        user_dict[key] = value
print(user_dict)
# Given two lists ["CA", "NJ", "RI"] and ["California", "New Jersey", "Rhode Island"]
# return a dictionary that looks like this {'CA': 'California', 'NJ': 'New Jersey', 'RI': 'Rhode Island'}.
# You can research the zip method to help you.
first_list = ["CA", "NJ", "RI"]
second_list = ["California", "New Jersey", "Rhode Island"]
new_list = list(zip(first_list, second_list))
towns_dict = {}
for i in range(0, len(new_list)):
    for key, value in new_list:
        towns_dict[key] = value
print(towns_dict)
# Create a dictionary with the key as a vowel in the alphabet and the value as 0.
# Your dictionary should look like this {'a': 0, 'e': 0, 'i': 0, 'o': 0, 'u': 0}. (Do not use the fromkeys method).
vowels_list = ["a", "e", "i", "o", "u"]
zero_list = []
for i in range(0, len(vowels_list)):
    zero_list.append(0)
merge_list = list(zip(vowels_list, zero_list))
vowels_dict = {}
for i in range(0, len(merge_list)):
    for key, value in merge_list:
        vowels_dict[key] = value
print(f"First attempt: {vowels_dict}")

vowels = {letter: 0 for letter in "aeiou"}
print(f"Second attempt: {vowels}")

vowels_dict2 = {}
for val in vowels_list:
    vowels_dict2[val] = 0
print(f"Third attempt: {vowels_dict2}")

# Create a dictionary starting with the key of the position of the letter and the value as the letter in the alphabet.
# You should return something like this (Hint - use chr(65) to get the first letter):
letters_list = list(string.ascii_uppercase)
number_list = list(range(1, len(letters_list)+1))
num_let_list = list(zip(number_list, letters_list))
letters_dict = {}
for i in range(0, len(num_let_list) + 1):
    for key, value in num_let_list:
        letters_dict[key] = value
print(f"First attempt: {letters_dict}")

letters_dict2 = dict(zip(range(1, 27), string.ascii_uppercase))
print(f"Second attempt: {letters_dict2}")

# Super Bonus
# 5.Given the string “awesome sauce” return a dictionary with the keys as vowels and the values as the count of vowels.
# Your dictionary should look like {‘a’: 2, ‘e’: 3, ‘i’: 0, ‘o’: 1, ‘u’: 1}

list_vowels = ["a", "e", "i", "o", "u"]
my_string = "awesome sauce"
zero_list = []
for i in range(0, len(vowels_list)):
    zero_list.append(0)
count_list = list(zip(vowels_list, zero_list))
count_vowels_dict = {}

for i in range(0, len(list_vowels)):
    for key, value in count_list:
        count_vowels_dict[key] = value + my_string.count(key)
print(count_vowels_dict)