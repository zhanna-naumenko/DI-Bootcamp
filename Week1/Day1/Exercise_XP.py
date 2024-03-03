#Exercise 1
print("Hello world\n" * 4)

#Exercise 2
print((99 ** 3) * 8)

#Exercise 3
#5 < 3 - False
# 3 == 3 - True
# 3 == "3" - False
# "3" > 3 - TypeError
# "Hello" == "hello" - False

#Exercise 4
computer_brand = "MSI"
print(f"I have a {computer_brand} computer")

#Exercise 5
name = "Zhanna"
age = 35
shoe_size = 37
info = f"My name is {name}. I was born {age} years ago. I like to walk, so I need a sneakers with {shoe_size} size."
print(info)

#Exercise 6
a = 12
b = 8
if a > b:
    print("Hello World")
elif b > a:
    print(f"Variable b = {b} is bigger than variable a = {a}")
else:
    print(f"Variable a = {a} is equal to variable b = {b}.")

#Exercise 7
my_num = int(input("Please enter the number: "))

if my_num % 2 == 0:
    print(f"Your number {my_num} is even.")
else:
    print(f"Your number {my_num} is odd.")

#Exercise 8
my_name = "ZHANNA"
user_name = (input("Please enter your name: ")).upper()

if my_name == user_name:
    print("Funny! We are namesakes;)")
else:
    print("We have different names.")

#Exercise 9
my_height = int(input("Please input your height in cm: "))

if my_height >= 145:
    print("You can ride a Roller Coaster!")
else:
    print("You need to grow some more to ride a Roller Coaster.")



