# Challenge 1: Letter Index Dictionary
user_word = input("Please enter a word: ")

letters_dict = {}

for index, letter in enumerate(user_word):
    if letter in letters_dict:
        letters_dict[letter].append(index)
    else:
        letters_dict[letter] = [index]

print(letters_dict)


# Challenge 2: Affordable Items
items_purchase = {"Water": "$1", "Bread": "$3", "TV": "$1,000", "Fertilizer": "$20"}
wallet = "$300"

#Showing the user products and their cost
for key,value in items_purchase.items():
    print(f"There is a product " + key + "which costs " + value)

#Showing the user how much money in the wallet
print(f"And you have {wallet} in your wallet.")

# cleaning the value of the dictionary to get clear numbers
for key, value in items_purchase.items():
    items_purchase[key] = value.replace("$","")
for key, value in items_purchase.items():
    items_purchase[key] = int(value.replace(",",""))

# cleaning the wallet string and convert it to integer
new_wallet = int(wallet.replace("$","").replace(",",""))

affordable_products = []

for key,value in items_purchase.items():
    # checking if the price more than we have in the wallet then we skip it
    if value > new_wallet:
        continue
    # if we have money in the wallet then we subtract
    # the cost of the product from wallet and add it to the affordable_products list
    elif new_wallet != 0:
        new_wallet -= value
        affordable_products.append(key)

# printing the message to the user with the final result
if affordable_products == []:
    print("Sorry, you can afford nothing from this list of the products.")
else:
    affordable_products.sort()
    print("You can afford:\n")
    for item in affordable_products:
        print(f"-{item}")



