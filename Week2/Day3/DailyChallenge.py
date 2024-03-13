import math

class Circle:
    def __init__(self, radius=None, diameter=None):
        if radius is not None:
            self.radius = radius
        elif diameter is not None:
            self.radius = diameter / 2
        else:
            raise ValueError("Please provide either radius or diameter.")

    @property
    def diameter(self):
        return self.radius * 2

    @property
    def area(self):
        return math.pi * self.radius ** 2

    def __str__(self):
        return f"Circle with radius {self.radius}"

    def __add__(self, other):
        if isinstance(other, Circle):
            return Circle(radius=self.radius + other.radius)
        else:
            raise TypeError("Unsupported operand type. Please provide another Circle instance.")

    def __lt__(self, other):
        return self.radius < other.radius

    def __eq__(self, other):
        return self.radius == other.radius

    def draw(self):
        # Bonus: Draw the circle using Turtle (requires the Turtle module)
        import turtle
        turtle.circle(self.radius)
        turtle.done()

# Example usage:
circle1 = Circle(radius=5)
circle2 = Circle(diameter=10)

print(circle1)
print(f"Diameter: {circle1.diameter}")
print(f"Area: {circle1.area:.2f}")

circle3 = circle1 + circle2
print(f"Combined Circle: {circle3}")

print(f"Is circle1 smaller than circle2? {circle1 < circle2}")
print(f"Are circle1 and circle2 equal? {circle1 == circle2}")