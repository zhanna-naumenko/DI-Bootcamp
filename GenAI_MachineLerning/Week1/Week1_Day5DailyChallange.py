import string


# Exercise 1 Write a script that inserts an item at a defined index in a list.
my_list = ["apple", "orange", "lemon"]
new_item = "kiwi"
my_list.insert(1, new_item)
print(my_list)

# Exercise 2 Write a script that counts the number of spaces in a string.

# user_text = input("Please enter your text: ")
# num_of_spaces = user_text.count(" ")
# print(num_of_spaces)

# Exercise 3 Write a script that calculates the number of upper case letters and lower case letters in a string.

# user_string2 = input("Please enter your text: ")
# upper_letters = string.ascii_uppercase
# lower_letters = string.ascii_lowercase
# num_of_upper = 0
# num_of_lower = 0
# for letter in user_string2:
#     if letter in upper_letters:
#         num_of_upper += 1
#     elif letter in lower_letters:
#         num_of_lower += 1
#
# print(f"The number of uppercase letters is {num_of_upper}, and of the lowercase letters is {num_of_lower}")

# Exercise 4 Write a function to find the sum of an array without using the built in function
def add(*args):
    sum_of_num = 0
    for item in args:
        sum_of_num += item
    return sum_of_num

print(add(*[5, 5, 5, 5]))

# Exercise 5 Write a function to find the max number in a list

def find_max(lst):
    max_num = lst[0]
    for item in lst:
        if item > max_num:
            max_num = item
    return max_num
user_list = [2, 10, 5, 52]
print(find_max(user_list))

# Exercise 6 Write a function that returns factorial of a number

def fact(n):
    return 1 if n <= 1 else n * fact(n-1)

print(fact(6))

# Exercise 7 Write a function that counts an element in a list (without using the count method):
def count_element(lst:list, val):
    num_item = 0
    for item in lst:
        if item == val:
            num_item += 1
    return num_item

user_list = [2, 10, 5, 52, 2, 2, 2]
user_list2 = ["a", "b", "c", "b", "b"]
print(count_element(user_list2, "b"))

# Exercise 8 Write a function that returns the L2-norm (square root of the sum of squares) of the sum of a list:

def l2_normalize(lst):
    lst_norm = sum([num**2 for num in lst]) ** 0.5
    return round(lst_norm)
user_list_norm = [1, 2, 2]
print(l2_normalize(user_list_norm))

# Exercise 9 Write a function to find if an array is monotonic (sorted either ascending of descending)

def is_monotonic(arr):
    if not arr or len(arr) == 1:
        return True
    increasing = decreasing = True
    for i in range(1, len(arr)):
        if arr[i] > arr[i - 1]:
            decreasing = False
        if arr[i] < arr[i - 1]:
            increasing = False
    return increasing or decreasing

user_list_mono = [7,6,5,5,2,0]
print(is_monotonic(user_list_mono))

# Exercise 10 Write a function that prints the longest word in a list.

def longest_word(lst):
    long_word = max(lst, key=lambda x: len(x))
    return long_word

print(longest_word(["abra", "cadabra", "boo"]))

# Exercise 11 Given a list of integers and strings, put all the integers in one list, and all the strings in another one.

def separation(lst):
    letters_list = []
    numbers_list = []
    for item in lst:
        if isinstance(item, str):
            letters_list.append(item)
        elif isinstance(item, int):
            numbers_list.append(item)
    return letters_list, numbers_list

print(separation([10, "abra", 15, "cadabra", "boo", 1, 2, 3]))

# Exercise 12 Write a function to check if a string is a palindrome

def palindrome(word):
    word = word.lower().replace(" ", "")
    if word == word[::-1]:
        return True
    return False
print(palindrome("banana"))
print(palindrome('radar'))

# Exercise 13 Write a function that returns the amount of words in a sentence with length > k
def check_length_of_word(words: str, number: int):
    words_list = words.split()
    num_of_words_more_than_number = 0
    for item in words_list:
        if len(item) > number:
            num_of_words_more_than_number += 1
    return num_of_words_more_than_number

my_string_to_check = "Hello! How you doing?"
print(check_length_of_word(my_string_to_check, 3))

# Exercise 14 Write a function that returns the average value in a dictionary (assume the values are numeric):

def dict_avg(dictionary):
    list_f_values = list(dictionary.values())
    avg_num = int(sum(list_f_values)/len(list_f_values))
    return avg_num

print(dict_avg({'a': 1,'b':2,'c':8,'d': 1}))

# Exercise 15 Write a function that returns common divisors of 2 numbers
def common_div(num1: int, num2: int):
    div_numbers = []
    for item in range(1, min(num1, num2)+1):
        if num1 % item == 0 and num2 % item == 0:
            div_numbers.append(item)
    return div_numbers

print(common_div(10,20))

# Exercise 16 Write a function that test if a number is prime
def prime_number(num):
    if num <= 1:
        return False
    else:
        is_prime = True  # Flag variable
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                is_prime = False
                break
        return is_prime

print(prime_number(10))
print(prime_number(11))

# Exercise 17 Write a function that prints elements of a list if the index and the value are even
def even_value_index(lst):
    even_values = []
    for index, item in enumerate(lst):
        if index % 2 == 0 and item % 2 == 0:
            even_values.append(index)
    return even_values
print(even_value_index([1,2,2,3,4,5]))


# Exercise 18 Write a function that accepts an undefined number of
# keyworded arguments and return the count of different types

def type_count(**kwargs):
    type_counts = {}
    for value in kwargs.values():
        t = type(value)
        if t in type_counts:
            type_counts[t] += 1
        else:
            type_counts[t] = 1
    return type_counts

print(type_count(a=1,b='string',c=1.0,d=True,e=False))


# Exercise 19 Write a function that mimics the builtin .split() method for strings.
# By default the function uses whitespace but it should be able to take an argument
# for any character and split with that argument.

def my_split(s: str, sep=None):
    result = []
    word = ""
    if sep is None:  # split by whitespace
        for char in s:
            if char.isspace():
                if word:  # avoid empty strings
                    result.append(word)
                    word = ""
            else:
                word += char
        if word:
            result.append(word)
    else:
        for char in s:
            if char == sep:
                result.append(word)
                word = ""
            else:
                word += char
        result.append(word)
    return result

print(my_split("Hello world! How are you?"))
print(my_split("apple,banana,cherry", sep=","))
print(my_split("one;two;three;four", sep=";"))


# Exercise 20 Convert a string into password format.

user_password = input("Please enter your password: ")
new_password = "*" * len(user_password)
print(new_password)