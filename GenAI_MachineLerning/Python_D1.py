# Exercise 1 : Boolean Logic
# 1.Declare a variable called first and assign it to the value "Hello World".
first = "Hello World"
print(first)

# 2.Write a comment that says "This is a comment."
# This is a comment.


# 3.Log a message to the terminal that says "I AM A COMPUTER!"
computer_message = "I AM A COMPUTER!"
print(computer_message)

# 4.Write an if statement that checks if 1 is less than 2 and if 4 is greater than 2.
# If it is, show the message "Math is fun."
if 1 < 2 and 4 > 2:
    print("Math is fun.")

# 5.Assign a variable called nope to an absence of value.
nope = None
print(nope)

# 6.Use the language’s “and” boolean operator to combine the language’s “true” value with its “false” value.
result = True and False
print(f"Result of True and False: {result}")

# 7.Calculate the length of the string "What's my length?"
user_string = "What's my length?"
length = len(user_string)
print(length)

# 8.Convert the string "i am shouting" to uppercase.
upper_string = "i am shouting".upper()
print(upper_string)

# 9.Convert the string "1000"to the number 1000.
string_to_number = int("1000")
# print(string_to_number*2)
print(type(string_to_number))

# 10.Combine the number 4 with the string "real" to produce "4real".
first_word = "4"
second_word = "real"
print(first_word + second_word)
print("4" + "real")

# 11.Record the output of the expression 3 * "cool".
# it will be the SyntaxError

# 12.Record the output of the expression 1 / 0.
# it will be ZeroDivisionError

# 13.Determine the type of [].
print(type([]))

# 14.Ask the user for their name, and store it in a variable called name.
name = input("Please enter your name: ")
print(name)

# 15.Ask the user for a number. If the number is negative, show a message that says "That number is less than 0!"
# If the number is positive, show a message that says "That number is greater than 0!" Otherwise,
# show a message that says "You picked 0!.

user_number = int(input("Please enter your number: "))

if user_number > 0:
    print("That number is greater than 0!")
elif user_number < 0:
    print("That number is less than 0!")
else:
    print("You picked 0!")

# 16.Find the index of "l" in "apple"
word = "apple"
find_index = word.index("l")
print(find_index)

# 17.Check whether "y" is in "xylophone".
word2 = "xylophone"
if "y" in word2:
    print("There is 'y' in the word xylophone.")
else:
    print("There is NO 'y' in the word xylophone.")

# 18.Check whether a string called my_string is all in lowercase.
my_string = "hello"

if my_string == my_string.lower():
    print("The string is all in lowercase.")
else:
    print("The string is not all in lowercase.")

# Exercise 2 : Cat’s and dog’s years

# Number of cat/dog years for the first human year
first_year = 15

# Number of cat/dog years for the second human year
second_year = 9

# Number of cat years added for each year after the second year
cat_next_years = 4

# Number of dog years added for each year after the second year
dog_next_years = 5

# Ask the user to enter their age and convert input to integer
user_year = int(input("Please enter your age: "))

# If the user is 1 year old
if user_year == 1:
    # For 1 human year, both cat and dog years equal 15
    print([1, 15, 15])

# If the user is 2 years old
elif user_year == 2:
    # For 2 human years:
    # 15 (first year) + 9 (second year) = 24
    print([2, 24, 24])

# If the user is older than 2 years
elif user_year > 2:
    # Calculate cat years:
    # 15 (first year) + 9 (second year) +
    # 4 years for each additional human year after 2
    cat_years = first_year + second_year + (user_year - 2) * cat_next_years

    # Calculate dog years:
    # 15 (first year) + 9 (second year) +
    # 5 years for each additional human year after 2
    dog_next_years = first_year + second_year + (user_year - 2) * dog_next_years

    # Print results as a list: [human years, cat years, dog years]
    print([user_year, cat_years, dog_next_years])

# If the user enters 0 or a negative number
else:
    # Show error message
    print("Not correct input.")
