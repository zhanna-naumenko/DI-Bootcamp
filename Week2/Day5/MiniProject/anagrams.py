from anagram_checker import *
import string

anagram_checker = AnagramChecker('sowpods.txt')
list_of_words = anagram_checker.load_word_list('sowpods.txt')

flag = True
while True:
    user_input = ((input('Please write a word if you want to check anagram, if not write /exit: ')).strip()).upper()
    if " " in user_input:
        print("The only one word accepted! Try again!")
    elif user_input.isalpha():
        if anagram_checker.is_valid_word(user_input):
            print(f"YOUR WORD :{user_input}")
            print("This is a valid English word.")
            # print(anagram_checker.get_anagrams(user_input))
            str_anagrams = ", ".join(anagram_checker.get_anagrams(user_input))
            print(f"Anagrams for your word: {str_anagrams}")
        else:
            print(f"Your {user_input} word is not correct.")
    elif user_input == ("/exit").upper():
        flag = False
        break
    else:
        print("Be careful! There are more than just letters in your word!")
