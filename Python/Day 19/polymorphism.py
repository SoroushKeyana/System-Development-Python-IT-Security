import math

class Shape:
    def area(self):
        pass

    def perimeter(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius**2

    def perimeter(self):
        return 2 * math.pi * self.radius

class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

    def perimeter(self):
        return 2 * (self.length + self.width)

class Triangle(Shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area(self):
        return 0.5 * self.base * self.height

    def perimeter(self):
        return 3 * self.base

circle = Circle(5)
rectangle = Rectangle(4, 6)
triangle = Triangle(3, 4)

shapes = [circle, rectangle, triangle]

for shape in shapes:
    if isinstance(shape, Shape):
        print(f"Shape Type: {shape.__class__.__name__}")
        print(f"Area: {shape.area()}")
        print(f"Perimeter: {shape.perimeter()}")
