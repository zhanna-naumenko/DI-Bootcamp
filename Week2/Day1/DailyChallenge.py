class Farm:
    def __init__(self, farm_name):
        self.farm_name = farm_name
        self.animals = {}

    def add_animal(self, animal, num_of_animals=1):
        if animal not in self.animals:
            self.animals[animal] = num_of_animals
        else:
            self.animals[animal] += 1


    def get_info(self):
        farm_info = f"{self.farm_name}'s farm\n"
        for animal, num_of_animals in self.animals.items():
            farm_info += f"{animal} : {num_of_animals}\n"
        farm_info += "E-I-E-I-0!"
        return farm_info

macdonald = Farm("McDonald")
macdonald.add_animal('cow', 5)
macdonald.add_animal('sheep')
macdonald.add_animal('sheep')
macdonald.add_animal('goat', 12)
print(macdonald.get_info())
