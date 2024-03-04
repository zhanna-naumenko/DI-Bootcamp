#Exercise 1
#1
my_fav_numbers = {3, 5, 12, 13, 15, 18, 21}
print(my_fav_numbers)
#2
my_fav_numbers.add(23)
my_fav_numbers.add(56)
print(my_fav_numbers)
#3
my_fav_numbers.pop()
print(my_fav_numbers)
#4
friend_fav_numbers = {4, 6, 9, 25, 29, 34}
#5
our_fav_numbers = my_fav_numbers.union(friend_fav_numbers)
print(our_fav_numbers)

#Exercise 2
my_tuple = (1, 2, 3, 4, 10) #it is not possible to add more integers to tuple,
# but I've read about it found that we can add some integers by concatenating
new_tuple = my_tuple + (6, 7)
print(new_tuple)

#Exercise 3
basket = ["Banana", "Apples", "Oranges", "Blueberries"]
#1
basket.remove("Banana")
print(basket)
#2
basket.remove("Blueberries")
print(basket)
#3
basket.append("Kiwi")
print(basket)
#4
basket.insert(0, "Apples")
print(basket)
#5
print(basket.count("Apples"))
#6
basket.clear()
#7
print(basket)

#Exercise 4
#1 float is a number with a dot. Integer is like a whole number without remainder and a float has it.
#2
my_list = [1.5, 2, 2.5, 3, 3.5, 4, 4.5, 5]
#3
my_numb = 1.5
list_numb = []
while my_numb <= 5:
    list_numb.append(my_numb)
    my_numb += 0.5
print(list_numb)

#Exercise 5
#1
for num in range(1, 21):
    print(num)

#2
for num in range(1, 21):
    if num % 2 == 0:
        print(num)

#Exercise 6
my_name = "Zhanna"
while True:
    user_name = input("Please enter Your name (enter 'Zhanna' if you want finish): ")
    if user_name == my_name:
        break
    else:
        print("We are not namesakes! Try again;)")
print("We are namesakes! Awesome!")

#Exercise 7
user_fruits = input("Please enter Your favorite fruits by separating them with a space: ")
list_fruits = list(user_fruits.split(" "))
print(list_fruits)
new_fruit = input("Please enter a name of any new fruit: ")
if new_fruit in user_fruits:
    print("You chose one of your favorite fruits! Enjoy!")
else:
    print("You chose a new fruit. I hope you enjoy")

#Exercise 8
#1
toppings = []
while True:
    user_topping = input("Please enter the toppings for pizza (enter 'quit'  when you are finished): ")
    toppings.append(user_topping)
    if user_topping == "quit":
        break
    else:
        print(f"You’ll add {user_topping} topping to your pizza.")
toppings.pop(-1)
#2
str_toppings = ", ".join(str(element) for element in toppings)
print(f"Your toppings are: {str_toppings}")
#3
total_price = 10 + 2.5 * len(toppings)
print(total_price)

#Exercise 9
