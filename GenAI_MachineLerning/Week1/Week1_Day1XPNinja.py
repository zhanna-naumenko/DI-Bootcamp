# Exercise 3 : Outputs
x = (1 == True)
y = (1 == False)
a = True + 4
b = False + 10

print("x is", x)
print("y is", y)
print("a:", a)
print("b:", b)

# Exercise 4 : How many characters in a sentence ?
my_text = """Lorem ipsum dolor sit amet, consectetur adipiscing elit, 
           sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. 
           Ut enim ad minim veniam, quis nostrud exercitation ullamco 
           laboris nisi ut aliquip ex ea commodo consequat. 
           Duis aute irure dolor in reprehenderit in voluptate velit 
           esse cillum dolore eu fugiat nulla pariatur. 
           Excepteur sint occaecat cupidatat non proident, 
           sunt in culpa qui officia deserunt mollit anim id est laborum."""
print(len(my_text))

# Exercise 5: Longest word without a specific character

while True:
    user_string = input("Please enter a string without 'a' character: ")
    if "a" in user_string:
        print("There is an 'a' character in the string. Try again.")
    elif user_string == "quit":
        print("Goodbye!")
        break
    else:
        print("Congratulation! You wrote the string without 'a' character.")