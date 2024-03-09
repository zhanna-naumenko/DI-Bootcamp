#Challenge 1

user_words = input("Please write the words separating them by coma: ")

sorted_words = sorted([word.strip() for word in user_words.split(',')])
print(",".join(sorted_words))

#Challenge 2
user_sentence = input("Please write your sentence: ")
list_of_words_in_sentence = list(user_sentence.split(" "))

def get_longest_word(list):
    '''Gets the longest word from the list'''
    longest_item = list[0]
    for item in list:
        if len(item) >= len(longest_item):
            longest_item = item
    return longest_item

print(get_longest_word(list_of_words_in_sentence))
