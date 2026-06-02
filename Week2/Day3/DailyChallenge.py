import math

class Circle:
    def __init__(self, radius, diameter):
        self.radius = radius
        self.diameter = diameter

    @classmethod
    def from_radius(cls, radius):
        return cls(radius=radius, diameter=radius * 2)


    @classmethod
    def from_diameter(cls, diameter):
        return cls(radius=diameter / 2, diameter=diameter)

    def circle_area(self):
        area = round(math.pi * self.radius**2, 3)
        return area

    def __str__(self):
        return f"The radius of the circle is: {self.radius}.\nThe diameter of the circle is: {self.diameter}"

    def __add__(self, other):
        new_circle = self.radius + other.radius
        return new_circle

    def __lt__(self, other):
        return self.radius < other.radius

    def __eq__(self, other):
        return self.radius == other.radius


circle1 = Circle(4, 8)
circle2 = Circle(2, 4)
print(circle1)
print(f"The circle's area is: {circle1.circle_area()}")
print(f"The new radius: {circle2.radius + circle1.radius}")
print(f"Which circle is bigger? {circle1 > circle2}")
print(f"Is the circles are equal? {circle1 == circle2}")