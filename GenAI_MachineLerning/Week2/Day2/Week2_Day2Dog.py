# Exercise 2: Dogs
class Dog:
    def __init__(self, name, age, weight):
        self.name = name
        self.age = age
        self.weight = weight

    def bark(self):
        return f"{self.name} is barking."

    def run_speed(self):
        return f"{self.name} is running with speed of {self.weight / (self.age *10)}km/h."

    def fight(self, other_dog):
        first_dog_strength = self.run_speed() * self.weight
        other_dog_strength = other_dog.run_speed() * other_dog.weight
        if first_dog_strength > other_dog_strength:
            return f"{self.name} won the {other_dog.name}"
        elif other_dog_strength > first_dog_strength:
            return f"{other_dog.name} won the {self.name}"
        else:
            return f"The strength of {self.name} is the same as {other_dog.name}."

# Step 2: Create dog instances
dog1 = Dog("Rex", 10, 50)
dog2 = Dog("Polo", 5, 35)
dog3 = Dog("Manny", 7, 40)

# Step 3: Test dog methods
print(dog1.bark())
print(dog2.run_speed())
print(dog1.fight(dog2))
