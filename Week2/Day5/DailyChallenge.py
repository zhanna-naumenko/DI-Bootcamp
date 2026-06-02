import random

#Part 1 : Quizz
# 1. What is a class?
# It's like a template that allows to create objects and defines the properties (called attributes)
# and behaviors (called methods) that all objects created from that class will have.

# 2.What is an instance?
#  An instance refers to a specific occurrence or realization of a class.
#  When you create an object from a class, we are creating an instance of that class.

# 3.What is encapsulation?
# Encapsulation is a concept in Python that allows to merge the data such as
# bundling data (attributes) and the methods (functions) within a class.

# What is abstraction?

# What is inheritance? Inheritance allows a new class to inherit attributes and methods from an existing class.
# The existing class is called the parent class and the new class is called the child class.

# What is multiple inheritance? Multiple inheritance it's when a class can inherit attributes and methods from more than one parent class.
# A child class can inherit from multiple parent classes, combining their functionality.

# What is polymorphism? Polymorphism allows objects of different classes to be treated as if they were objects of a common superclass.
# Different classes can define the same method or attribute name, but with different implementations.

# What is method resolution order or MRO?  It is an order in which Python looks for methods and attributes in a class hierarchy.
# It determines how Python resolves method and attribute references when dealing with inheritance and multiple inheritance.

#Part 2
suits_list = ["Hearts", "Diamonds", "Clubs", "Spades"]
value_list = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]



class Card:
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value



class Deck:
    def __init__(self):
        self.units_deck = []
        self.suits = ["Hearts", "Diamonds", "Clubs", "Spades"]
        self.values = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]

    def create_deck(self):
        '''Create a list of deck cards'''
        for suit in self.suits:
            for value in self.values:
                card = Card(suit, value)
                self.units_deck.append(card)
        return self.units_deck

    def shuffle_deck(self):
        '''Shuffle the deck of cards'''
        return random.shuffle(self.units_deck)

    def deal(self):
        '''Takes one random card from the deck and delete it'''
        return self.units_deck.pop()




user_deck = Deck()
#creating a deck o cards
user_deck.create_deck()

#shuffeling deck of cards
user_deck.shuffle_deck()

# printing one of the card from the list of deck cards
print(user_deck.units_deck[0].suit, user_deck.units_deck[0].value)

# printing the whole deck
for card in user_deck.units_deck:
    print(f"{card.suit} {card.value}")

#printing the length of the deck before deleting the card
print(len(user_deck.units_deck))

# deleting the card
card = user_deck.deal()

# printing the length of the deck after deleting the card
print(len(user_deck.units_deck))

# printing the card which was deleted
print(f"{card.suit} {card.value}")




