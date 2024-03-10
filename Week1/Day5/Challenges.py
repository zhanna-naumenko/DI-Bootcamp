import string

#Exercise 1

def change_value(user_list, value, index):
    '''Inserts an item at a defined index in a list'''
    user_list.insert(index, value)
    return user_list

my_list = ["apple", "cherry", "mango", "banana"]
print(change_value(user_list=my_list, value="pine", index=2))



#Exercise 2
# def count_spaces(user_string):
#     '''Counting the number of spaces in the string'''
#     list_of_val = list(user_string)
#     num_of_spaces = 0
#     for item in list_of_val:
#         if item == " ":
#             num_of_spaces += 1
#     return num_of_spaces
#
# my_string = input("Please write a sentence: ")
# print(count_spaces(my_string))


#Exercise 3

# def count_upper_lower(user_string):
#     '''Calculates the number of upper case letters and lower case letters in a string'''
#     num_upper_letters = 0
#     num_lower_letters = 0
#     for item in user_string:
#         if item in string.ascii_uppercase:
#             num_upper_letters += 1
#         elif item in string.ascii_lowercase:
#             num_lower_letters += 1
#     print(f"The number of uppercase letters is: {num_upper_letters} letters\n "
#           f"The number of uppercase letters is: {num_lower_letters} letters")
#
# my_str = input("Please write a sentence: ")
# count_upper_lower(my_str)

#Exercise 4

def num_sum(user_list):
    sum_of_items = 0
    for item in user_list:
        sum_of_items += item
    return sum_of_items

my_test = [5, 12, 3]
print(num_sum(my_test))

#Exercise 5

def max_num(user_list):
    max_item = 0
    for item in user_list:
        if max_item <= item:
            max_item = item
    return max_item

my_test = [5000, 12, 30, 100]
print(max_num(my_test))

#Exercise 6




