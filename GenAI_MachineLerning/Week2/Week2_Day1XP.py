# Exercise 1: Cats

class Cat:
    def __init__(self, cat_name, cat_age):
        self.name = cat_name
        self.age = cat_age

# Step 1: Create cat objects
cat1 = Cat("Olly", 5)
cat2 = Cat("Daisy", 13)
cat3 = Cat("Busik", 7)

# Step 2: Create a function to find the oldest cat
def find_oldest_cat(val1, val2, val3):
    """Find the oldest cat"""
    objects_list = [val1, val2, val3]
    oldest_cat = max(objects_list, key=lambda x: x.age)
    return oldest_cat.name, oldest_cat.age

# Step 3: Print the oldest cat's details
print(f"The oldest cat is {find_oldest_cat(cat1, cat2, cat3)[0]}, and is {find_oldest_cat(cat1, cat2, cat3)[1]} years old.")

# Exercise 2 : Dogs
class Dog:
    def __init__(self, name, height):
        self.name = name
        self.height = height

    def bark(self):
        print(f"{self.name} goes woof!")

    def jump(self):
        print(f"{self.name}  jumps {self.height * 2} cm high!")

davids_dog = Dog("Kevin", 20)
sarahs_dog = Dog("Boby", 15)

davids_dog.bark()
davids_dog.jump()
print("______________________________")
sarahs_dog.bark()
sarahs_dog.jump()

def compare_sizes(dog1, dog2):
    """Compare two dogs"""
    if dog1.height > dog2.height:
        return f"The size of the {dog1.name} is bigger than the size of the {dog2.name}."
    else:
        return f"The size of the {dog2.name} is bigger than the size of the {dog1.name}."

print(compare_sizes(sarahs_dog, davids_dog))

# Exercise 3 : Who’s the song producer?
class Song:
    def __init__(self, lyrics):
        self.lyrics = lyrics

    def sing_me_a_song(self):
        for val in self.lyrics:
            print(val)

stairway = Song(["There’s a lady who's sure", "all that glitters is gold", "and she’s buying a stairway to heaven"])
stairway.sing_me_a_song()

# Exercise 4 : Afternoon at the Zoo
class Zoo:
    def __init__(self, zoo_name):
        self.zoo_name = zoo_name
        self.animals = []

    def add_animal(self, new_animal):
        if new_animal not in self.animals:
            self.animals.append(new_animal)
        else:
            print(f"The animal {new_animal} already exists.")

    def get_animals(self):
        print(f"In the Zoo {self.zoo_name} there is such animals: ")
        for animal in self.animals:
            print(f"- {animal}")


    def sell_animal(self, animal_sold):
        if animal_sold in self.animals:
            self.animals.remove(animal_sold)
            print(f"The zoo {self.zoo_name} sold {animal_sold} animal.")
        else:
            print(f"The animal {animal_sold} does not in the zoo.")

    def sort_animals(self):
        sorted_animals = {}
        self.animals.sort()
        for animal in self.animals:
            first_letter = animal[0]

            if first_letter not in sorted_animals:
                sorted_animals[first_letter] = []

            sorted_animals[first_letter].append(animal)

        return sorted_animals

    def get_groups(self):
        dict_animals = self.sort_animals()
        for key, animal in dict_animals.items():
            print(f"{key}: {animal}")



brooklyn_safari = Zoo("Brooklyn Safari")
brooklyn_safari.add_animal("Giraffe")
brooklyn_safari.add_animal("Bear")
brooklyn_safari.add_animal("Baboon")
brooklyn_safari.get_animals()
brooklyn_safari.sell_animal("Bear")
brooklyn_safari.get_animals()
print(brooklyn_safari.sort_animals())
brooklyn_safari.get_groups()











