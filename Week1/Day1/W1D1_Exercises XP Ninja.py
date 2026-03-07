#Exercise 1

# When we run python3 in cmd we see the message 'Python 3.10.11 (tags/v3.10.11:7d4cc5a, Apr  5 2023, 00:38:17) [MSC v.1929 64 bit (AMD64)] on win32
# Type "help", "copyright", "credits" or "license" for more information.'
# When we run the command python3 in the command line,
# we can call it without being in the executable directory due to how the operating system's environment and PATH variable are set up.

# Exercise 2

# When we run C:\Users\MSI>py in cmd we see the message:
# 'Python 3.10.4 (tags/v3.10.4:9d38120, Mar 23 2022, 23:13:41) [MSC v.1929 64 bit (AMD64)] on win32
# Type "help", "copyright", "credits" or "license" for more information.'
# Typically the same as with previous command

#Exercise 3

# Predict the output of the following code snippets:

# 3 <= 3 < 9 - True
# 3 == 3 == 3 - True
# bool(0) - False
# bool(5 == "5") - False
# bool(4 == 4) == bool("4" == "4") - True
# bool(bool(None)) - False
# x = (1 == True) - True
# y = (1 == False)
# a = True + 4
# b = False + 10
#
# print("x is", x) - x is True
# print("y is", y) - y is False
# print("a:", a) - a: 5
# print("b:", b) - b: 10

# Exercise 4

my_text = "Lorem ipsum dolor sit amet, consectetur adipiscing elit, " \
          "sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. " \
          "Ut enim ad minim veniam, quis nostrud exercitation ullamco " \
          "laboris nisi ut aliquip ex ea commodo consequat. " \
          "Duis aute irure dolor in reprehenderit in voluptate velit " \
          "esse cillum dolore eu fugiat nulla pariatur. " \
          "Excepteur sint occaecat cupidatat non proident, " \
          "sunt in culpa qui officia deserunt mollit anim id est laborum."

print(len(my_text))

# Exercise 5

end_of_game = False

while not end_of_game:
    user_input = (input("Please input a sentence without the character “A” or if you want to end the game input quit: ")).lower()
    if user_input == "quit":
        break
    elif "a" not in user_input:
        print("Good job!")
    else:
        print("The letter 'A' is in the sentence. Please try again.")