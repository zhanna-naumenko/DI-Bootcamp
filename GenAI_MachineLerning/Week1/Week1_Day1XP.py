# Exercise 1: Hello World
print("Hello World\n" * 4)

# Exercise 2: Some Math
print(99**3*8)

# Exercise 3: What is the output?
# >>> 5 < 3 False
# >>> 3 == 3 True
# >>> 3 == "3" False
# >>> "3" > 3 Error
# >>> "Hello" == "hello" Error
# print(5 < 3)
# print(3 == 3)
# print(3 == "3")
# print("3" > 3)
# print("Hello" == "hello")

# Exercise 4: Your computer brand
computer_brand = "MSI"
print(f"I have a {computer_brand} computer.")

# Exercise 5: Your information
name = "Zhanna"
age = 37
shoe_size = 37
info = f"Hi! My name is {name} and I am {age} years old, and I have {shoe_size} shoes."
print(info)

# Exercise 6: A & B
a = 4
b = 7
if a > b:
    print("Hello World")
else:
    print("A is not bigger than B")

# Exercise 7: Odd or Even
user_number = int(input("Enter a number: "))

if user_number % 2 == 0:
    print("Your number is even.")
else:
    print("Your number is odd.")

# Exercise 8: What’s your name?
my_name = "Zhanna"
user_name = input("Enter a name: ")

if user_name == my_name:
    print("Wow! We are namesakes♥")
else:
    print("You have different name than I am ☻")

# Exercise 9: Tall enough to ride a roller coaster
print("Welcome to a roller coaster")

user_height = int(input("Please enter your height in centimeters: "))
if user_height >= 145:
    print("You are tall enough to ride to ride a roller coaster.")
else:
    print(f"Sorry, you need to grow more for {145-user_height}cm to ride a roller coaster.")