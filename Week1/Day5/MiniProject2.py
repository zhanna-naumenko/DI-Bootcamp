import random

hangman_pictures = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

wordslist = ['correction', 'childish', 'beach', 'python', 'assertive', 'interference', 'complete', 'share',
             'credit card', 'rush', 'south']
word = random.choice(wordslist)

### YOUR CODE STARTS FROM HERE ###

print("Welcome to the Hangman game!")

# Create a list called 'shown_word' with '*' for each character in the 'word'
shown_word = ["*" for x in range(len(word))]
print(f"The word is {''.join(shown_word)} and there is {len(word)} letters in it.")

num_of_lives = 6

end_of_game = False

while not end_of_game:
    choice_of_letter = (input("Please enter a letter: ")).lower()
    for position in range(len(word)):
        letter = word[position]
        if letter == choice_of_letter:
            shown_word[position] = letter
    if choice_of_letter not in word:
        num_of_lives -= 1
        if num_of_lives == 0:
            end_of_game = True
            print("You lost")
    print(''.join(shown_word))
    print(hangman_pictures[num_of_lives])
    if "*" not in shown_word:
        end_of_game = True
        print("You win.")


