import string
# Caesar Cypher

list_of_letters = list(string.ascii_lowercase)
print(list_of_letters)
print(len(list_of_letters))

user_string = input("Enter a word: ").lower()
step_num = int(input("Enter number of step: "))

new_word = ""

for letter in user_string:
    if letter in list_of_letters:
        old_index = list_of_letters.index(letter)
        new_index = (old_index + step_num) % len(list_of_letters)
        new_word += list_of_letters[new_index]
    else:
        new_word += letter

print(new_word)




