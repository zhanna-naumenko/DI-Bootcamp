class Farm:
    def __init__(self, farm_name):
        self.farm_name = farm_name
        self.animals = {}

    def add_animal(self, animal_type, count=1):
        if animal_type not in self.animals:
            self.animals[animal_type] = count
        else:
            self.animals[animal_type] += count

        return self.animals


    def get_info(self):
        print(f"{self.farm_name}")
        for animal in self.animals:
            print(f"{animal} : {self.animals[animal]}")
        print("E-I-E-I-0!")

    def get_animal_types(self):
        animals_types = []
        for key in self.animals.keys():
            animals_types.append(key)
        animals_types.sort()
        return animals_types


# Test the code
macdonald = Farm("McDonald")
macdonald.add_animal('cow', 5)
macdonald.add_animal('sheep')
macdonald.add_animal('sheep')
macdonald.add_animal('sheep', 3)
macdonald.add_animal('goat', 12)
macdonald.add_animal('goat')
macdonald.get_info()
print(macdonald.get_animal_types())