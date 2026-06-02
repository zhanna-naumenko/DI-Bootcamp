import string
import os
dir_path = os.path.dirname(os.path.realpath(__file__))

#Part I
class Text:
    def __init__(self, user_text):
        self.user_text = user_text

    @classmethod
    def from_file(cls, file_name):
        with open(dir_path + f"\\{file_name}", "r") as file_text:
            return cls(file_text.read())

    def word_frequency(self):
        translator = str.maketrans("", "", string.punctuation)
        clean_text = self.user_text.translate(translator)
        list_of_words = clean_text.lower().split()
        dict_of_word_frequency = {}
        for item in list_of_words:
            dict_of_word_frequency[item] = list_of_words.count(item)
        print(dict_of_word_frequency)

    def get_common_word(self):
        translator = str.maketrans("", "", string.punctuation)
        clean_text = self.user_text.translate(translator)
        list_of_words = clean_text.lower().split()
        dict_of_word_frequency = {}
        for item in list_of_words:
            dict_of_word_frequency[item] = list_of_words.count(item)
        most_common_word = max(dict_of_word_frequency, key=dict_of_word_frequency.get)
        print(most_common_word)

    def get_unique_words(self):
        translator = str.maketrans("", "", string.punctuation)
        clean_text = self.user_text.translate(translator)
        list_of_words = clean_text.lower().split()
        dict_of_word_frequency = {}
        unique_words = []
        for item in list_of_words:
            dict_of_word_frequency[item] = list_of_words.count(item)
        for key in dict_of_word_frequency.keys():
            unique_words.append(key)
        print(unique_words)




my_text = Text("A good book would sometimes cost as much as a good house house.")
my_text.word_frequency()
my_text.get_common_word()
my_text.get_unique_words()

#Part II

file_text = Text.from_file('the_stranger.txt')
file_text.word_frequency()
file_text.get_common_word()
file_text.get_unique_words()
