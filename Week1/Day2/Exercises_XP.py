#1
my_fav_numbers = {3, 5, 12, 13, 15, 18, 21}
print(my_fav_numbers)
my_fav_numbers.add(23)
my_fav_numbers.add(56)
print(my_fav_numbers)
my_fav_numbers.pop()
print(my_fav_numbers)
friend_fav_numbers = {4, 6, 9, 25, 29, 34}
our_fav_numbers = my_fav_numbers.union(friend_fav_numbers)
print(our_fav_numbers)

#2
my_tuple = ("banana", "orange", "flower") #the tuples are unchangeable

#3
basket = ["Banana", "Apples", "Oranges", "Blueberries"]
print(basket)
basket.remove("Banana")
basket.remove("Blueberries")
basket.insert(3, "Kiwi")
basket.insert(0, "Apples")
print(basket)
print(basket.count("Apples"))