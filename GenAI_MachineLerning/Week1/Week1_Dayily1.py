# Challenge 1: Multiples of a Number

user_number = int(input("Please enter a number: "))
user_length = int(input("Please enter a length: "))
user_numbers_list = []

for item in range(1, user_length + 1):
    user_numbers_list.append(user_number*item)

print(user_numbers_list)

# Challenge 2: Remove Consecutive Duplicate Letters

user_word = input("Please enter a word: ")

if not user_word:
    print("")
else:
    new_word = user_word[0]
    for char in user_word[1:]:
        if char != new_word[-1]:
            new_word += char
    print(new_word)



