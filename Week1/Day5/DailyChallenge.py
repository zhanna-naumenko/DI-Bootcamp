#Challenge 1

user_words = input("Please write the words separating them by coma: ")
#deleted spaces
user_words = user_words.replace(" ", "")
#put every word in to the list
user_list_of_words = list(user_words.split(","))
#sorting the list
user_list_of_words.sort()
print(",".join(user_list_of_words))

#Challenge 2
user_sentence = input("Please write your sentence: ")
list_of_words_in_sentence = list(user_sentence.split(" "))
print(list_of_words_in_sentence)

def get_longest_word(list):
    '''Gets the longest word from the list'''
    longest_item = len(list[0])
    for item in list:
        if len(item) >= longest_item:
            longest_item == item
    return item

print(get_longest_word(list_of_words_in_sentence))
