import datetime
from calendar import weekday
import string


# Exercise 1 : Functions Exercises
#1.Write the following functions difference this function takes in
# two parameters and returns the difference between the two
def difference(num1, num2):
    return num1 - num2

print(difference(4, 2))

# 2.print_day. This function takes in one parameter (a number from 1-7)
# and returns the day of the week (1 is Sunday, 2 is Monday, 3 is Tuesday etc.).
# If the number is less than 1 or greater than 7, the function should return None
day_of_week = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]

def print_day(num):
    if num in range(0, len(day_of_week)):
        print(day_of_week[num - 1])
    else:
        print("The number is incorrect.")

print_day(4)

# 3.last_element. this function takes in one parameter (a list) and returns the last value in the list.
# It should return None if the list is empty.
def last_element(lst):
    if len(lst) == 0:
        return None
    return lst[-1]

random_list = [1,2,3,4,5]
print(last_element(random_list))

# 4.number_compare
# this function takes in two parameters (both numbers). If the first is greater than the second,
# this function returns “First is greater.” If the second number is greater than the first,
# the function returns “Second is greater.” Otherwise, the function returns “Numbers are equal.”
def number_compare(num1, num2):
    if num1 > num2:
        return "First is greater."
    elif num1 < num2:
        return "Second is greater."
    else:
        return "Numbers are equal."

print(number_compare(6, 4))

# 5.single_letter_count
# this function takes in two parameters (two strings).
# The first parameter should be a word and the second should be a letter.
# The function returns the number of times that letter appears in the word.
# The function should be case insensitive (does not matter if the input is lowercase or uppercase).
# If the letter is not found in the word, the function should return 0.

def single_letter_count(word, letter):
    if type(word) != str or type(letter) != str:
        return "The type of message is wrong."
    elif type(word) == str and type(letter) == str:
        if letter.lower() in word.lower():
            return f"The letter '{letter}' in word '{word}' appears {word.lower().count(letter.lower())} times."
        else:
            return f"The letter '{letter}' is not in the word {word}."

print(single_letter_count("amazing", "u"))

# 6.multiple_letter_count this function takes in one parameter (a string) and returns
# a dictionary with the keys being the letters and the values being the count of the letter.
def multiple_letter_count(word):
    if type(word) != str:
        return "The type of message is wrong."
    if type(word) == str:
        word_dict = {char: word.count(char) for char in word}
        return word_dict
    return None

print(multiple_letter_count("amazing"))

# 7.list_manipulation this function should take in three parameters (a list, command, location and value).
#
# If the command is “remove” and the location is “end”, the function should remove the last value in the list and return the value removed
# If the command is “remove” and the location is “beginning”, the function should remove the first value in the list and return the value removed
# If the command is “add” and the location is “beginning”, the function should add the value (fourth parameter) to the beginning of the list and return the list
# If the command is “add” and the location is “end”, the function should add the value (fourth parameter) to the end of the list and return the list

def list_manipulation(lst, command, location, value=None):
    if type(lst) != list:
        return "The type of message is wrong."
    if command == "remove":
        if location == "beginning":
            return lst.pop(0)
        elif location == "end":
            return lst.pop()
    if command == "add":
        if location == "beginning":
            lst.insert(0,value)
        elif location == "end":
            lst.append(value)
        return lst
    return None


print(list_manipulation([1,2,3], "remove", "end"))

# 8.is_palindrome A Palindrome is a word, phrase, number, or other sequence of characters which reads the same backward or forward.
# This function should take in one parameter and returns True or False depending on whether it is a palindrome.
# As a bonus, allow your function to ignore whitespace and capitalization so that is_palindrome('a man a plan a canal Panama')
# returns True.
def is_palindrome(word):
    if type(word) != str:
        return "The type of message is wrong."
    if type(word) == str:
        word = word.replace(" ", "")
        if word.lower() == word.lower()[::-1]:
            return True

        else:
            return False
    return None

print(is_palindrome('tacocat'))

# 9. frequency. This function accepts a list and a search_term (this will always be a primitive value)
# and returns the number of times the search_term appears in the list.
def frequency(lst, value):
    if type(lst) != list:
        return "The type of message is wrong."
    if value in lst:
        return lst.count(value)
    return None


print(frequency([1,2,3,4,4,4,4,4], 4))
print(frequency([True, False, True, True], False))

# 10.flip_case This function accepts a string and a letter and reverses the case of all occurances of the letter in the string

def flip_case(word, letter):
    if type(word) != str:
        return "The type of message is wrong."
    result = ""

    for char in word:
        if char.lower() == letter.lower():
            if char.islower():
                result += char.upper()
            else:
                result += char.lower()
        else:
            result += char

    return result
print(flip_case("Hardy har har", "h"))

# 11.multiply_even_numbers This function accepts a list of numbers and returns the product of all even numbers in the list.This function accepts a list of numbers and returns the product of all even numbers in the list.
def multiply_even_numbers(lst):
    if type(lst) != list:
        print("The type of message is wrong.")
    mult_even = 1
    for val in lst:
        if val % 2 == 0:
            mult_even *= val
    return mult_even

print(multiply_even_numbers([2,3,4,5,6]))

# 12. mode This function accepts a list of numbers
# and returns the most frequent number in the list of numbers. You can assume that the mode will be unique.
def mode(lst):
    if type(lst) != list:
        return "The type of message is wrong."
    return max(set(lst), key=lst.count)

print(mode([2,4,1,2,3,2]))

# 13.capitalize This function accepts a string and returns the same string with the first letter capitalized.
def capitalize(word):
    if type(word) != str:
        return "The type of message is wrong."
    return word.replace(word[0],word[0].upper())

print(capitalize("matt"))

# 14. compact This function accepts a list and returns a list of values that are truthy values.
def compact(lst):
    return [item for item in lst if item]

print(compact([0,1,2,"",[], False, {}, None, True, "I"]))

# 15. partition This function accepts a list and a callback function
# (which you can assume returns True or False). The function should iterate over each element
# in the list and invoke the callback function at each iteration.
# If the result of the callback function is True, the element should go into one list if it’s False,
# the element should go into another list. When it’s finished, partition should return both lists inside of one larger list.
def is_even(num):
    return num % 2 == 0

def partition(lst, func):
    even_list = []
    odd_list = []
    new_list = []
    for val in lst:
        if is_even(val) == True:
            even_list.append(val)
        elif is_even(val) == False:
            odd_list.append(val)
    new_list.append(even_list)
    new_list.append(odd_list)
    return new_list
print(partition([1,2,3,4,5,6], is_even))

# 16. intersection This function should accept
# a two dimensional list and return a list with the values that are the same in each list.

def intersection(lst1, lst2):
    return list(set(lst1).intersection(lst2))

print(intersection([1,2,3,4], [2,3,4]))

# 17. once This function accepts a function and returns a new function that can only be invoked once.
# If the function is invoked more than once, it should return None. Hint you will need to define a new
# function inside of your once function and return that function.
# You can add properties to your inner function to see if it has run already.
# Super bonus
# Research what decorators are and refactor your once code to use a decorator so that you can run

# def add(a,b):
#     return a + b
def once(func):
    has_run = False
    def wrapper(*args, **kwargs):
        nonlocal has_run

        if has_run:
            return None
        has_run = True
        return func(*args, **kwargs)
    return wrapper
@once
def add(a, b):
    return a + b
one_addition = once(add)

print(one_addition(2,2))
print(one_addition(2,2))

# Exercise 2 : Functions Exercises#2
# 1.Complete the solution so that it reverses the string passed into it.

my_string = "hello World"
def revers_word(word):
    if type(word) != str:
        return "The type of message is wrong."
    word.replace(" ", "")
    return word[::-1]

print(revers_word(my_string))

# 2.Looking for a benefactor

def last_donation(lst, new_av):
    av_lst = sum(lst) / len(lst)
    if av_lst > new_av:
        return "Your expectation is too low."
    elif av_lst < new_av:
        return (new_av * (len(lst) + 1)) - sum(lst)

    return None

print(last_donation([14, 30, 5, 7, 9, 11, 15], 92))
print(last_donation([14, 30, 5, 7, 9, 11, 15], 15))

# Sum of a sequence
def sequence_sum(begin, end, step):
    if begin > end:
        return 0
    total = 0
    current = begin
    while current <= end:
        total += current
        current += step

    return total

print(sequence_sum(2,2,2))

# Max diff
def max_diff(lst):
    return max(lst) - min(lst)

print(max_diff([1, 10, 3, -4]))
# Count the similey faces!
SMILES = [":)", ";)", ":-)", ";-)", ":D",";D", ":-D", ";-D", ":~)",";~)", ":~D", ";~D"]
def countSmileys(lst):
    total = 0
    for val in lst:
        if val in SMILES:
            total += 1
    return total
print(countSmileys([';]', ':[', ';*', ':$', ';-D']))

# Sentence Count
SENT_LIST = [".", "!", "?"]
def numb_sentence(word):
    total = 0
    for val in word:
        if val in SENT_LIST:
            total += 1
    return total

print(numb_sentence("I want to ask you. And you need to ask me!"))

# Tortoise Racing
def race(v1, v2, g):
    if v1 > v2:
        return None
    seconds = int((g / (v2 - v1)) * 3600)

    hours = seconds // 3600
    minutes = (seconds % 3600) // 60
    seconds = seconds % 60
    return [hours, minutes, seconds]
print(race(80, 91, 37))

# Calculate String Rotation
def rotation_count(s1, s2):
    # If lengths differ, cannot be rotation
    if len(s1) != len(s2):
        return -1

    # If already equal
    if s1 == s2:
        return 0

    # Double the first string
    doubled = s1 + s1

    # Find where s2 appears
    index = doubled.find(s2)

    if index == -1:
        return -1

    return index

print(rotation_count("dog", "god"))








