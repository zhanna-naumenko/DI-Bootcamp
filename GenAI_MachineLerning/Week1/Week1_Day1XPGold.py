# Exercise 1 : Hello World-I love Python
print("Hello world\n" * 4 + "I love python\n" * 4)

# Exercise 2 : What is the Season ?

user_month = int(input("Please enter the number of the month from 1 to 12: "))

if user_month in range(3, 6):
    print("It is Spring month.")
elif user_month in range(6, 9):
    print("It is Summer month.")
elif user_month in range(9, 12):
    print("It is Autumn month.")
else:
    print("It is Winter month.")
