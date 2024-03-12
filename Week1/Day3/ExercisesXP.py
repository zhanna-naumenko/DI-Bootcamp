#Exercise 1
keys = ['Ten', 'Twenty', 'Thirty']
values = [10, 20, 30]

print(dict(zip(keys, values)))
##################################

#Exercise 2
family = {"rick": 43, 'beth': 13, 'morty': 5, 'summer': 8}
total_price = 0
for keys, values in family.items():
    if 3 <= values <= 12:
        price = 10
        print(f"{keys.capitalize()}'s ticket costs {price}$.")
        total_price += price
    elif values > 12:
        price = 15
        print(f"{keys.capitalize()}'s ticket costs {price}$.")
        total_price += price

print(f"The family's total price is: {total_price}$")
#Bonus
family_names = input("Please enter names of your family by separating them with a space:")
family_ages = input("Please enter ages of your family by separating it with a space:")

list_names = list(family_names.split(" "))
list_ages = list(family_ages.split(" "))
dict_family = dict(zip(list_names, list_ages))
print(dict_family)
total_price = 0
for keys, values in dict_family.items():
    if 3 <= int(values) <= 12:
        price = 10
        print(f"{keys.capitalize()}'s ticket costs {price}$.")
        total_price += price
    elif int(values) > 12:
        price = 15
        print(f"{keys.capitalize()}'s ticket costs {price}$.")
        total_price += price

print(f"The family's total price is: {total_price}$")
#########################################################

#Exercise 3
brand = {'name': 'Zara',
         'creation_date': 1975,
         'creator_name': 'Amancio Ortega Gaona',
         'type_of_clothes': ['men', 'women', 'children', 'home'],
         'international_competitors': ['Gap', 'H&M', 'Benetton'],
         'number_stores': 7000,
         'major_color':{'France': 'blue','Spain': 'red','US': ('pink', 'green')}}

#3
brand['number_stores'] = 2
print(brand)

#4
print(f"Zara's clients are: {', '.join(brand['type_of_clothes'][0:-1])}")

#5
brand["country_creation"] = "Spain"
print(brand)

#6
if 'international_competitors' in brand:
    brand['international_competitors'].append("Desigual")
print(brand)

#7
brand.pop('creation_date')
print(brand)

#8
print(brand['international_competitors'][-1])

#9
for item in (brand['major_color']['US']):
    print(item)
#10
for key, value in brand.items():
    if isinstance(value, (list, dict)):
        print(f"Number of values for key '{key}': {len(value)}")
    else:
        print(f"Number of values for key '{key}': 1")
#11
for keys, values in brand.items():
    print(keys)

#12
more_on_zara = {}
more_on_zara["creation_date"] = 1975
more_on_zara["number_stores"] = 10000
print(more_on_zara)
############################################

#Exercise 4
users = ["Mickey","Minnie","Donald","Ariel","Pluto"]

#1
disney_users_A = {user: index for index, user in enumerate(users)}
print(disney_users_A)

#2
disney_users_B = {index: user for index, user in enumerate(users)}
print(disney_users_B)

#3
users.sort()
disney_users_C = {user: index for index, user in enumerate(users)}
print(disney_users_C)

#4.1The characters, which names contain the letter “i”
disney_users_A1 = {user: index for index, user in enumerate(users) if "i" in user}
print(disney_users_A1)

#4.2The characters, which names start with the letter “m” or “p”
disney_users_A2 = {user: index for index, user in enumerate(users) if user[0].lower() in ["m", "p"]}
print(disney_users_A2)








