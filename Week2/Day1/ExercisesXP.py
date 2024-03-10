#Exercise 1

class Cat:
    def __init__(self, cat_name, cat_age):
        self.name = cat_name
        self.age = cat_age

abyssinian_cat = Cat('Fluffy', 3)
egyptian_cat = Cat("Daisy", 12)
nebelung_cat = Cat('Poppy', 5)

list_of_cats = [abyssinian_cat.__dict__, egyptian_cat.__dict__, nebelung_cat.__dict__]
print(list_of_cats)

def get_oldest_cat(cat_list):
    max_age = 0
    oldest_cat_name = ''

    for cat_dict in cat_list:
        age_value = cat_dict.get('age')
        name_value = cat_dict.get('name')

        if age_value is not None:
            if age_value > max_age:
                max_age = age_value
                oldest_cat_name = name_value

    print(f'The oldest cat is {oldest_cat_name}, and is {max_age} years old.')


get_oldest_cat(list_of_cats)

#Exercise 2

class Dog:
    def __init__(self, name, height):
        self.name = name
        self.height = height
    def bark(self):
        print(f'{self.name} goes woof!')
    def jump(self):
        x = self.height * 2
        print(f'{self.name} jumps {x} cm high!')

davids_dog = Dog('Rex', 50)
print(davids_dog.name, davids_dog.height)
davids_dog.jump()
davids_dog.bark()

sarahs_dog = Dog('Teacup', 20)
print(sarahs_dog.name, sarahs_dog.height)
sarahs_dog.jump()
sarahs_dog.bark()

freds_dog = Dog('Zuzu', 100)
milies_dog = Dog('Kuku', 60)

list_of_dogs = [davids_dog.__dict__, sarahs_dog.__dict__, freds_dog.__dict__, milies_dog.__dict__]

def get_bigger_dog(list):
    max_height = 0
    name_of_biggest_dog = ""
    for dog_dict in list:
        name_value = dog_dict.get("name")
        height_value = dog_dict.get("height")
        if height_value is not None:
            if height_value > max_height:
                max_height = height_value
                name_of_biggest_dog = name_value
    return name_of_biggest_dog

print(get_bigger_dog(list_of_dogs))

#Exercise 3

class Song:
    def __init__(self, lyrics):
        self.lyrics = lyrics

    def sing_me_a_song(self):
        print(*self.lyrics, sep="\n")

stairway= Song(["There’s a lady who's sure","all that glitters is gold", "and she’s buying a stairway to heaven"])
stairway.sing_me_a_song()

# Exercise 4
class Zoo:
    def __init__(self, zoo_name):
        self.name = zoo_name
        self.animals = []

    def add_animal(self, *new_animal):
        if self.name not in self.animals:
            self.animals.extend(new_animal)

    def get_animals(self):
        for item in self.animals:
            print(item)

    def sell_animal(self, animal_sold):
        for item in self.animals:
            if item in self.animals and animal_sold == item:
                self.animals.remove(item)

    def sort_animals(self):
        for _ in self.animals:
            self.animals.sort()
        grouped_animals = {}
        for animal in self.animals:
            first_letter = animal[0].upper()
            if first_letter not in grouped_animals:
                grouped_animals[first_letter] = []

            grouped_animals[first_letter].append(animal)
        return grouped_animals

    def get_groups(self):
        for key, animals in grouped_animals.items():
            print(f"Animals of group {key}: {', '.join(animals)}")


market_zoo = Zoo("Aqua Villa")
market_zoo.animals = ["Elephant", "Lion"]
print(f"The animals in Aqua Villa Zoo: {market_zoo.animals}")

#added the new animals in the list of animals
market_zoo.add_animal("Alligator", "Camel", "Kangaroo", "Baboo", "Bear")
print(f"The Aqua Villa Zoo gets more animals: {market_zoo.animals}")

#get an animals one by one
market_zoo.get_animals()

#delete the animal from the list if it in it
market_zoo.sell_animal("Lion")
print(market_zoo.animals)

#sorted and groups animals by first letter
grouped_animals = market_zoo.sort_animals()
print(market_zoo.sort_animals())

#prints the animal/animals inside each group
print("\nAnimals Inside Each Group:")
market_zoo.get_groups()

#new object
ramat_gan_safari = Zoo("Ramat Gan Safari")
ramat_gan_safari.animals = ["Ape", "Snake", "Lion", "Penguin", "Lama"]
print(f"The animals in Ramat Gan Safari: {ramat_gan_safari.animals}")

#added the new animals in the list of animals
ramat_gan_safari.add_animal("Camel", "Kangaroo", "Alligator", "Bear")
print(ramat_gan_safari.animals)

#get an animals one by one
ramat_gan_safari.get_animals()

#delete the animal from the list if it in it
ramat_gan_safari.sell_animal("Kangaroo")
print(ramat_gan_safari.animals)


#sorted and groups animals by first letter
grouped_animals = ramat_gan_safari.sort_animals()
print(ramat_gan_safari.sort_animals())

#prints the animal/animals inside each group
print("\nAnimals Inside Each Group:")
ramat_gan_safari.get_groups()










