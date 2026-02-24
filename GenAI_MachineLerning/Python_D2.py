import string

# 1.Print all values
first_list = [1, 2, 3, 4]
[print(i) for i in first_list]


# 2.Multiply values by 20
second_list = [1, 2, 3, 4]
[print(i * 20) for i in second_list]


# 3.First letters
names_list = ["Elie", "Tim", "Matt"]
new_list = [name[0] for name in names_list]
print(new_list)


# 4.Even numbers (single solution)
third_list = [1, 2, 3, 4, 5, 6]
even_list = [num for num in third_list if num % 2 == 0]
print(even_list)


# 5.Intersection of two lists
list1 = [1, 2, 3, 4]
list2 = [3, 4, 5, 6]
intersection = [num for num in list1 if num in list2]
print(intersection)


# 6.Reverse words + lowercase
name_list = ["Elie", "Tim", "Matt"]
new_name_list = [name.lower()[::-1] for name in name_list]
print(new_name_list)


# 7.Common letters between two strings
first_string = "first"
second_string = "third"
common_letters = [letter for letter in first_string if letter in second_string]
print(common_letters)


# 8.Numbers divisible by 12
list_div = [num for num in range(1, 101) if num % 12 == 0]
print(list_div)


# 9.Remove vowels
vowels = 'aeiouAEIOU'
my_str = "amazing"
list_consonants = [char for char in my_str if char not in vowels]
print(list_consonants)


# 10.Generate [[0,1,2],[0,1,2],[0,1,2]]
big_list = [[i for i in range(3)] for _ in range(3)]
print(big_list)


# 11.Generate nested growing lists
big_list = [[i for i in range(10)] for _ in range(10)]
print(big_list)

