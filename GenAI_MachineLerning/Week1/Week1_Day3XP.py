# Exercise 1: Converting Lists into Dictionaries
keys = ['Ten', 'Twenty', 'Thirty']
values = [10, 20, 30]
new_dict = {}

for i in range(len(keys)):
    new_dict[keys[i]] = values[i]

print(new_dict)

# Exercise 2: Cinemax #2
family = {"rick": 43, 'beth': 13, 'morty': 5, 'summer': 8}
total_bill = 0

for key in family.keys():
    value = family[key]
    if value < 3:
        total_bill += 0
    elif 3 <= value <= 12:
        total_bill += 10
    else:
        total_bill += 15

print(f"The final bill for the family is ${total_bill}")

# Exercise 3: Zara
brand = {"name": "Zara",
"creation_date": 1975,
"creator_name": "Amancio Ortega Gaona",
"type_of_clothes": ["men", "women", "children", "home"],
"international_competitors": ["Gap", "H&M", "Benetton"],
"number_stores": 7000,
"major_color":{"France": "blue","Spain": "red", "US": ["pink", "green"]}}

# Change the value of number_stores to 2.
brand["number_stores"] = 2
print(brand)

# Print a sentence describing Zara’s clients using the type_of_clothes key.
print("Zara’s clients using such kind of type clothes for:")
for val in brand["type_of_clothes"]:
    print(f"-{val}")

# Add a new key country_creation with the value Spain.
brand["country_creation"] = "Spain"
print(brand)

# Check if international_competitors exists and, if so, add “Desigual” to the list.
for key in brand:
    if key == "international_competitors":
        brand["international_competitors"].append("Desigual")
print(brand["international_competitors"])

# Delete the creation_date key.
brand.pop("creation_date")
print(brand)
# Print the last item in international_competitors.
print(brand["international_competitors"][-1])
# Print the major colors in the US.
print(f"The major colors in the US is: ")
for val in brand["major_color"]["US"]:
    print(f"-{val}")
# Print the number of keys in the dictionary.
print(len(brand.keys()))
# Print all keys of the dictionary.
print("All keys of the dictionary:")
for item in brand.keys():
    print(f"-{item}")

# Create another dictionary called more_on_zara with creation_date and number_stores.
# Merge this dictionary with the original brand dictionary and print the result.

more_on_zara = {"creation_date": 1975, "number_stores": 7000}
merged_dict = brand | more_on_zara
print(merged_dict)

# Exercise 4: Disney Characters
users = ["Mickey", "Minnie", "Donald", "Ariel", "Pluto"]

# 1. Create a dictionary that maps characters to their indices:
dict_users1 = {}
for item in users:
    dict_users1[item] = users.index(item)

print(dict_users1)

# 2. Create a dictionary that maps indices to characters:
dict_users2 = {}
for item in users:
    dict_users2[users.index(item)] = item

print(dict_users2)

# 3. Create a dictionary where characters are sorted alphabetically and mapped to their indices:
sorted_users = users.copy()
sorted_users.sort()
# print(sorted_users)
dict_users3 = {}
for item in sorted_users:
    dict_users3[item] = sorted_users.index(item)

print(dict_users3)
