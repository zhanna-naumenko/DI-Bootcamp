import random

user_string = input("Please enter your string. The length should be 10 characters long: ")

if len(user_string) > 10:
    print("Your string is too long.")
elif len(user_string) < 10:
    print("String not long enough.")
elif len(user_string) == 10:
    print("Perfect string")
    print(f"The first letter: {user_string[0]}")
    print(f"The last letter: {user_string[-1]}")
    string_of_letters = ""
    for letter in user_string:
        string_of_letters += letter
        print(string_of_letters)
    list_user = list(user_string)
    random.shuffle(list_user)
    print(f"Shuffled string: {"".join(list_user)}")






