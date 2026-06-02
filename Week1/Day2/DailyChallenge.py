#Challenge 1
number = int(input("Please enter the number: "))
length = int(input("Please enter the length: "))

my_list = []
while len(my_list) < length:
    for num in range(1, length + 1):
        my_list.append(number * num)
    break
print(my_list)

#Challenge 2
user_word = input("Please enter the word: ")

list_word = list(user_word)
print(list_word)
result = ""
prev_char = None
for char in list_word:
    if char != prev_char:
        result += char
    prev_char = char

print(f"The word is: {result}")

