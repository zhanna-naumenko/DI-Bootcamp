import random

my_str = input("Please enter some text: ")

if len(my_str) < 10:
    print("Your string is not long enough.")
elif len(my_str) == 10:
    print("Your string is perfect!")
else:
    print("Your string is too long.")

print(my_str[0], my_str[-1])

for letter in range(1, len(my_str) + 1):
    print(my_str[:letter])

my_list = list(my_str)
random.shuffle(my_list)
print(''.join(my_list))
