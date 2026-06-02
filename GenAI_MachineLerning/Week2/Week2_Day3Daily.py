import math
import turtle

class Circle:
    def __init__(self, diameter=None, radius=None):
        if diameter is None and radius is None:
            raise ValueError("You must specify a diameter or a radius")
        if radius is not None:
            self.radius = radius
        else:
            self.radius = diameter/2

    @property
    def radius(self):
        return self._radius

    @radius.setter
    def radius(self, value):
        self._radius = value

    @property
    def diameter(self):
        return self._radius * 2

    @diameter.setter
    def diameter(self, value):
        self._radius = value / 2

    @property
    def area(self):
        return math.pi * self.radius ** 2

    def __str__(self):
        return f"The radius of the circle: {self.radius}"

    def __repr__(self):
        return f"Circle({self.radius})"

    def __add__(self, other):
        if isinstance(other, Circle):
            return Circle(radius=self.radius + other.radius)
        return NotImplemented

    def __gt__(self, other):
        if not isinstance(other, Circle):
            return NotImplemented
        return self.radius > other.radius

    def __lt__(self, other):
        if not isinstance(other, Circle):
            return NotImplemented
        return self.radius < other.radius

    def __eq__(self, other: "Circle"):
        if isinstance(other, Circle):
            return self.radius == other.radius
        raise TypeError("The type is not correct")


c1 = Circle(radius=5)
c2 = Circle(diameter=20)

print(c1)
print(repr(c2))
print(c1 + c2)
print(c1==c2)
print(c2>c1)
print(c2<c1)
list_circles = [
    Circle(radius=3),
    Circle(radius=7),
    Circle(radius=1),
]

list_circles.sort()

print(list_circles)


def draw_circles(circles):
    t = turtle.Turtle()

    for circle in circles:
        t.circle(circle.radius * 10)  # scale for visibility
        t.penup()
        t.forward(circle.radius * 25)
        t.pendown()

    turtle.done()

draw_circles(list_circles)


