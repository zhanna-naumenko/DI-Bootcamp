import random
# Exercise 1: Quizz
# Answer the following questions:
#
# 1.What is a class?  A class is a blueprint used
# to create objects. It defines the attributes (data)
# and methods (functions) that the created objects will have.

# 2.What is an instance? An instance is an object
# created from a class. Each instance has its own
# data while sharing the behavior defined in the class.

# 3.What is encapsulation? Encapsulation is the concept of restricting
# direct access to an object's internal data and allowing interaction
# with it only through defined methods or properties. It helps protect data and keep it controlled.

# 4.What is abstraction? Abstraction means hiding complex implementation details and exposing only the necessary
# functionality to the user. The user interacts with what the object does, without needing to know how it works internally.

#5. What is inheritance? Inheritance is when one class (child class) inherits attributes and methods
# from another class (parent class). It allows code reuse and helps organize related classes.

# 6.What is multiple inheritance? Multiple inheritance is when a class inherits
# from more than one parent class, meaning it can receive functionality from multiple sources.

# 7.What is polymorphism? Polymorphism allows different classes to use methods with the same name
# but different implementations. The same method call can behave differently depending on the object that calls it

# 8.What is method resolution order or MRO? Method Resolution Order (MRO) is the order Python follows to search for methods
# and attributes in a class hierarchy, especially when inheritance or multiple inheritance is used.

# Exercise 2: Create a deck of cards class

class Card:
    def __init__(self, suit: str, value: str):
        self.suit = suit
        self.value = value

    def __str__(self):
        return f"{self.suit} {self.value}"


class Deck:

    def __init__(self):
        self.cards = []
        self.made_deck()

    def made_deck(self):
        suit_list = ["Hearts", "Diamonds", "Clubs", "Spades"]
        value_list = ["A","2","3","4","5","6","7","8","9","10","J","Q","K"]
        for suit in suit_list:
            for value in value_list:
                self.cards.append(Card(suit, value))

    def shuffle_deck(self):
        if len(self.cards) != 52:
            self.made_deck()
        return random.shuffle(self.cards)

    def deal(self):
        if len(self.cards) == 0:
            return "No cards left"
        return self.cards.pop()

# create a deck
deck = Deck()

# check number of cards
print("Cards in deck:", len(deck.cards))

# shuffle the deck
deck.shuffle_deck()
print("Deck shuffled!")

# deal one card
card = deck.deal()
print("Dealt card:", card)

# check remaining cards
print("Cards left:", len(deck.cards))

# deal 5 cards
print("\nDealing 5 cards:")
for _ in range(5):
    print(deck.deal())

# deal all remaining cards
print("\nDealing all remaining cards...")
while deck.cards:
    deck.deal()

# try dealing when empty
print("\nTrying to deal from empty deck:")
print(deck.deal())



