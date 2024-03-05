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
result = []
[result.append(letter) for letter in list_word if letter not in result]
print("".join(result))
