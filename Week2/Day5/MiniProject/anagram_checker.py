import os


dir_path = os.path.dirname(os.path.realpath(__file__))

class AnagramChecker:
    def __init__(self, word_list_file):
        self.word_list = self.load_word_list(word_list_file)

    def load_word_list(self, word_list_file):
        try:
            with open(word_list_file, 'r') as file:
                return [word.strip() for word in file.readlines()]
        except FileNotFoundError:
            print(f"Error: Word list file '{word_list_file}' not found.")
            return []

    def is_valid_word(self, user_word):
        for item in self.word_list:
            if item == user_word.upper():
                return True

    def get_anagrams(self, user_word):
        list_of_anagrams = []
        for item in self.word_list:
            if len(item) == len(user_word.upper()):
                if sorted(item) == sorted(user_word.upper()):
                # if sorted(list(item)) == sorted(list(user_word.upper())):
                    list_of_anagrams.append(item)
        return list_of_anagrams






if __name__ == "__main__":
    anagram_checker = AnagramChecker('sowpods.txt')
    # print(anagram_checker.word_list)

    print(anagram_checker.is_valid_word("team"))
    print(anagram_checker.get_anagrams("sadder"))

