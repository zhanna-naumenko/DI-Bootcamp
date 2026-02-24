import string

# 1.List of tuples to dictionary
user_list = [("name", "Elie"), ("job", "Instructor")]

user_dict = {key: value for key, value in user_list}
print(user_dict)

# 2.Combine two lists into dictionary (zip + comprehension)
first_list = ["CA", "NJ", "RI"]
second_list = ["California", "New Jersey", "Rhode Island"]

towns_dict = {key: value for key, value in zip(first_list, second_list)}

print(towns_dict)

# 3.Vowels dictionary with value 0
vowels_dict = {vowel: 0 for vowel in "aeiou"}
print(vowels_dict)

# 4.Position → alphabet letter
letters_dict = {i: chr(64 + i) for i in range(1, 27)}
print(letters_dict)

# BONUS — count vowels in string
list_vowels = ["a", "e", "i", "o", "u"]
my_string = "awesome sauce"

count_vowels_dict = {
    vowel: my_string.count(vowel)
    for vowel in list_vowels
}

print(count_vowels_dict)
