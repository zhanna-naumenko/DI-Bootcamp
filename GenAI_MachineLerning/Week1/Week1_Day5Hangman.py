import random

wordslist = ['correction', 'childish', 'beach', 'python', 'assertive', 'interference', 'complete', 'share',
             'credit card', 'rush', 'south']

HANGMANPICS = [
r''' 
  +---+
  |   |
      |
      |
      |
      |
=========
''',
r'''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''',
r'''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''',
r'''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========
''',
r'''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''',
r'''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''',
r'''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
'''
]
word = random.choice(wordslist)
marks_stars = "_" * len(word)
print(marks_stars)
print(f"There are {len(word)} letters in this word.")

guessed_letters = set()
num_of_attempts = 0

while num_of_attempts < 7:
    user_input = input("Please guess a letter: ").lower()

    if len(user_input) != 1 and not user_input.isalpha():
        print("You must enter a single letter. Please try again.")
        continue

    if user_input in guessed_letters:
        print(f"You already guessed this letter {user_input}. Please try to input another letter.")
        continue

    guessed_letters.add(user_input)
    if user_input not in word:
        print("There is no such letter in the word. Please try again.")
        print(f"{HANGMANPICS[num_of_attempts]}")
        num_of_attempts += 1

    current_word = ""
    for letter in word:
        if letter in guessed_letters:
            current_word += letter
        else:
            current_word += "_"

    print(current_word)

    if "_" not in current_word:
        print("🎉 You won!")
        break

else:
    print(f"Game over! The word was: {word}")