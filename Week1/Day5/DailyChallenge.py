#Challenge 1

user_words = input("Please write the words separating them by coma: ")

user_words = user_words.replace(" ", "")

user_list_of_words = list(user_words.split(","))
user_list_of_words.sort()
print(",".join(user_list_of_words))

#Challenge 2
user_sentence = input("Please write your sentence: ")
list_of_words_in_sentence = list(user_sentence.split(" "))
print(list_of_words_in_sentence)

def longest_word(list):
    lengths = [len(item) for item in list]
    index_for_longest_word = lengths.index(max(lengths))
    word_with_max_letters = list[index_for_longest_word]
    print(word_with_max_letters)


longest_word(list_of_words_in_sentence)
