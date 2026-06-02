import re
import string

class Text:
    def __init__(self, text):
        self.text = text

    def word_frequency(self, word: str):
        list_of_words = self.text.lower().split()
        if word in list_of_words:
            num_of_occurrences = list_of_words.count(word)
            return num_of_occurrences
        else:
            return "Word Not Found"

    def most_common_word(self):
        list_of_words = self.text.split()
        dict_of_words = {}
        for word in list_of_words:
            if word in dict_of_words:
                dict_of_words[word] += 1
            else:
                dict_of_words[word] = 1
        return max(dict_of_words, key=dict_of_words.get)

    def unique_words(self):
        list_of_words = self.text.split()
        set_of_words = set(list_of_words)
        return list(set_of_words)

    @classmethod
    def from_file(cls, file_path):
        with open(file_path, "r") as f:
            content_text = f.read()
            return cls(content_text)



class TextModification(Text):

    def remove_punctuation(self):
        return self.text.translate(str.maketrans('', '', string.punctuation))

    def remove_stop_words(self):
        stop_words = {
            "a", "an", "the", "and", "or", "is", "in", "on", "at", "to",
            "for", "with", "of", "by", "as", "that", "this", "it", "from",
            "be", "are", "was", "were", "has", "had", "but"
        }
        words = self.text.split()
        filtered_words = [word for word in words if word.lower() not in stop_words]
        return " ".join(filtered_words)

    def remove_special_characters(self):
        return re.sub(r'[^a-zA-Z\s]', '', self.text)




text = "Hello world! Hello everyone. This is Python. Python is great."

txt = Text(text)
print(txt.word_frequency("hello"))        # 2
print(txt.most_common_word())             # "hello"
print(txt.unique_words())                 # Unique words in text

mod = TextModification(text)
print(mod.remove_punctuation())           # "Hello world Hello everyone This is Python Python is great"
print(mod.remove_stop_words())            # "hello world hello everyone python python great"
print(mod.remove_special_characters())    # "Hello world Hello everyone This is Python Python is great"