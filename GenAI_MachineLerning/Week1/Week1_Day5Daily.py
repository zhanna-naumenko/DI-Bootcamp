# Challenge 1: Sorting

def sorted_words(words: str):
    list_of_words = list(words.split(","))
    list_of_words.sort()
    new_string = ", ".join(list_of_words)
    return new_string

def main():
    user_words = input("Enter your words separated by commas: ")
    print(f"Your words are: {sorted_words(user_words)}")

main()


# Challenge 2: Longest Word
def longest_word(words: str):
    list_of_words = list(words.split(" "))
    max_len = 0
    max_word = ""
    for index, word in enumerate(list_of_words):
        len_word = len(word)
        if len_word > max_len:
            max_len = len_word
            max_word = list_of_words[index]
    return max_word

def main_words():
    user_words = input("Enter your words separated by commas: ")
    print(f"The longest word is: {longest_word(user_words)}")

main_words()