# from collections import Counter
#Challenge 1
user_word = input("Please enter a word: ")
val_num = {}
for index, val in enumerate(user_word):
    if val not in val_num:
        val_num[val] = []
    val_num[val].append(index)
print(val_num)
#####################################

#Challenge 2
items_purchase = {
  "Phone": "$999",
  "Speakers": "$300",
  "Laptop": "$5,000",
  "PC": "$1200"
}

wallet = "$1"

items_purchase = {item: value.replace("$", "").replace(",", "") for item, value in items_purchase.items()}
wallet = wallet.replace("$","")

print(items_purchase)
print(wallet)

afford_list = []

for keys, values in items_purchase.items():
    if int(values) <= int(wallet):
        afford_list.append(keys)

if afford_list:
    print(sorted(afford_list))
else:
    print("Nothing")

