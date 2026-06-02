import random
from ExercisesXP import Dog

#Exercise 3
class PetDog(Dog):
    def __init__(self, name, age, weight, trained=False):
        super().__init__(name, age, weight)
        self.trained = trained

    def train(self):
        self.bark()
        self.trained = True


    def play(self, *names):
        dogs_name = list(names)
        print(f"{self.name}, {', '.join(dogs_name)} all play together")

    def do_a_trick(self):
        random_string = ["does a barrel roll", "stands on his back legs", "shakes your hand", "plays dead"]
        if self.trained == True:
            print(f"{self.name} {random_string[random.randint(0, len(random_string))]}")
        else:
            print("This dog is not trained.")

pet_dog1 = PetDog("Toto", 5, 12)
pet_dog2 = PetDog("Momo", 3, 4)
pet_dog3 = PetDog("Susu", 6, 10)
pet_dog2.play("Pipi", "Susu")
print(pet_dog1.train())

pet_dog3.do_a_trick()
pet_dog1.do_a_trick()
