#Exercise 1

class Pets():
    def __init__(self, animals):
        self.animals = animals

    def walk(self):
        for animal in self.animals:
            print(animal.walk())

class Cat():
    is_lazy = True

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def walk(self):
        return f'{self.name} is just walking around'

class Bengal(Cat):
    def sing(self, sounds):
        return f'{sounds}'

class Chartreux(Cat):
    def sing(self, sounds):
        return f'{sounds}'

class Siamese(Cat):

    def __init__(self, name, age):
        super().__init__(name, age)


#Exercise 2

class Dog:

    def __init__(self, name, age, weight):
        self.name = name
        self.age = age
        self.weight = weight

    def bark(self):
        print(f"{self.name} is barking.")

    def run_speed(self):
        dog_speed = int(self.weight / self.age * 10)
        return dog_speed

    def fight(self, other_dog):
        winner = int(self.run_speed() * self.weight)
        second_dog = int(other_dog.run_speed() * other_dog.weight)
        if winner < second_dog:
            print(self.name)
        else:
            print(other_dog.name)


#Exercise 4

class Family:

    def __init__(self, last_name):
        self.last_name = str(last_name)
        self.members = []

    def born(self, **kwargs):
        self.members.append(kwargs)
        print(f"Congratulation! {kwargs['name']} joined to the {self.last_name} family.")

    def is_18(self, name):
        for member in self.members:
            if member["name"] == name and member["age"] >= 18:
                return True
        return False
    def family_presentation(self):
        for member in self.members:
            print(member["name"], member["age"], member["gender"], member["is_child"])



#Exercise 5
class TheIncredibles(Family):

    def __init__(self, last_name, members):
        super().__init__(last_name)
        for member in members:
            super().born(**member)

    def use_power(self, name):
        for member in self.members:
            if member["name"] == name and member["age"] >= 18:
                print(f"{member['name']} can use the power: {member['power']}")
                return
        raise Exception(f"{name} is not over 18 years old.")

    def incredible_presentation(self):
        print("Here is our powerful family!")
        super().family_presentation()




if __name__ == '__main__':
    # Exercise 1 outputs

    cat1 = Bengal("Toto", 5)
    cat2 = Chartreux("Muchu", 7)
    cat3 = Siamese("Mimi", 10)
    all_cats = [cat1, cat2, cat3]
    sara_pets = Pets(all_cats)
    sara_pets.walk()


    # Exercise 2 outputs
    dog1 = Dog("Puppy", 12, 23)
    dog2 = Dog("Fluffy", 7, 15)
    dog3 = Dog("Rex", 6, 35)
    print(dog1.run_speed())
    dog2.bark()
    dog3.fight(dog1)
    dog2.fight(dog3)


    # Exercise 4 outputs
    user_family = Family("Pirson")
    user_family.born(name="John", age=35, gender="Male", is_child=False)
    user_family.born(name="Yana", age=7, gender="Female", is_child=True)
    user_family.born(name="Molly", age=3, gender="Female", is_child=True)
    print(user_family.members)
    print(user_family.is_18('John'))
    user_family.family_presentation()


    user2_family = Family("Oldman")
    user2_family.born(name="Michael", age=35, gender="Male", is_child=False)
    user2_family.born(name="Sarah", age=32, gender="Female", is_child=False)
    print(user2_family.members)
    print(user2_family.is_18('Sarah'))
    user2_family.family_presentation()

    # Exercise 5 outputs
    incredibles_members = [{'name': 'Michael', 'age': 35, 'gender': 'Male', 'is_child': False, 'power': 'fly', 'incredible_name': 'MikeFly'},
        {'name': 'Sarah', 'age': 32, 'gender': 'Female', 'is_child': False, 'power': 'read minds', 'incredible_name': 'SuperWoman'}]

    incredibles_family = TheIncredibles(last_name="Incredibles", members=incredibles_members)

    incredibles_family.incredible_presentation()

    incredibles_family.born(name="Baby Jack", age=1, gender="Male", is_child=True, power="Unknown Power",
                            incredible_name="TinyJack")
    incredibles_family.incredible_presentation()



