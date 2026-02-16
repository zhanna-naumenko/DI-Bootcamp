import string

# Exercise : List #1
# Write the following Python code to do the following (complete ALL of these using list comprehension).
# Given a list [1,2,3,4], print out all the values in the list.
first_list = [1, 2, 3, 4]
for i in first_list:
    print(i)

# Given a list [1,2,3,4], print out all the values in the list multiplied by 20.
second_list = [1, 2, 3, 4]
for i in second_list:
    print(i*20)

# Given a list [“Elie”, “Tim”, “Matt”], return a new list with only the first letter ([“E”, “T”, “M”]).
names_list = ["Elie", "Tim", "Matt"]
new_list = []
for i in names_list:
    fist_letter = i[0]
    new_list.append(fist_letter)
print(new_list)

# Given a list [1,2,3,4,5,6] return a new list of all the even values ([2,4,6]).
third_list = [1,2,3,4,5,6]
even_list = list(filter(lambda x: x % 2 == 0, third_list))
even_list2 = []
for i in even_list:
    if i % 2 == 0:
        even_list2.append(i)
print(even_list)
print(even_list2)

# Given two lists [1,2,3,4] and [3,4,5,6], return a new list that is the intersection of the two ([3,4]).
list1 = [1,2,3,4]
list2 = [3,4,5,6]
new_list = list(set(list1) & set(list2))
print(new_list)

# Given a list of words [“Elie”, “Tim”, “Matt”] return a new list with each word reversed and in lower case ([‘eile’, ‘mit’, ‘ttam’]).
name_list = ["Elie", "Tim", "Matt"]
new_name_list = []
for i in name_list:
    new_name_list.append(i.lower()[::-1])
print(new_name_list)

# Given two strings “first” and “third”, return a new string with all the letters present in both words ([“i”, “r”, “t”]).
first_string = "first"
second_string = "third"
new_list_letters = list(set(first_string) & set(second_string))
print(new_list_letters)

# For all the numbers between 1 and 100, return a list with all the numbers that are divisible by 12 ([12, 24, 36, 48, 60, 72, 84, 96]).
list_div = []
for i in range(1, 101):
    if i % 12 == 0:
        list_div.append(i)
print(list_div)
# Given the string “amazing”, return a list with all the vowels removed ([‘m’, ‘z’, ‘n’, ‘g’]).
vowels = 'aeiouAEIOU'
my_str = "amazing"
list_consonants = []
for i in my_str:
    if i not in vowels:
        list_consonants.append(i)
print(list_consonants)

# Generate a list with the value [[0, 1, 2], [0, 1, 2], [0, 1, 2]].
small_list = []
big_list = []
for i in range(0, 3):
    small_list.append(i)
    big_list.append(small_list)
print(big_list)
# Generate a list with the value:
small_list = []
big_list = []
for i in range(0, 10):
    small_list.append(i)
    big_list.append(small_list)
print(big_list)