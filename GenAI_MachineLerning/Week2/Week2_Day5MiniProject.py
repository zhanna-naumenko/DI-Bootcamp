class AnagramChecker:
    def __init__(self, word_list_file: str):
        """
        Initialize the AnagramChecker by loading words from a file.
        All words are converted to lowercase for case-insensitive comparison.
        """
        self.words = set()  # using a set for faster lookup
        try:
            with open(word_list_file, "r") as f:
                for line in f:
                    # Remove any surrounding whitespace/newlines and convert to lowercase
                    word = line.strip().lower()
                    if word:  # skip empty lines
                        self.words.add(word)
        except FileNotFoundError:
            raise FileNotFoundError(f"The file '{word_list_file}' was not found.")

    def is_valid_word(self, word: str):
        return word.lower() in self.words

    def is_anagram(self, word1, word2):
        return sorted(word1.lower()) == sorted(word2.lower())
        # word1 = sorted(list(word1.lower()))
        # word2 = sorted(list(word2.lower()))
        # if word1 == word2:
        #     return True
        # return False

    def get_anagrams(self, user_word):
        anagrams = []
        user_word = user_word.lower()
        for word in self.words:
            if self.is_anagram(word, user_word) and word != user_word:
                anagrams.append(word)
        return anagrams

anagram = AnagramChecker("sowpods.txt")
print(anagram.is_valid_word("Meat"))
print(anagram.is_anagram("meet", "teme"))
print(anagram.get_anagrams("meat"))

