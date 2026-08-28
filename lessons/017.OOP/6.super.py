from math import pi


# super() is a function from a child to be used to call methods from the parent class used to
# extend functionality of parent class inherited functions
class Shape:
    def __init__(self, color, filled):
        self.color = color
        self.filled = filled

    # extending functionality
    def describe(self):
        print(
            f"It is {self.color} and it is {"Filled" if self.filled == True else "Not filled"}"
        )


class Circle(Shape):
    def __init__(self, color, filled, raduis):
        super().__init__(color, filled)
        self.raduis = raduis

    # note if you did not use the super function it will just overide the parent defnition
    def describe(self):
        super().describe()
        print(f"It is a circle withe area of {2 * pi * self.raduis}")


class Square(Shape):
    def __init__(self, color, filled, width):
        super().__init__(color, filled)
        self.width = width

    def describe(self):
        super().describe()
        print(f"It is a square withe area of {self.width * self.width}")


class Triangle(Shape):
    def __init__(self, color, filled, width, height):
        super().__init__(color, filled)
        self.width = width
        self.height = height

    def describe(self):
        super().describe()
        print(f"It is a Triangle withe area of {1/2 * self.width * self.height}")


circle = Circle("red", True, 5)
square = Square("blue", False, 6)
triangle = Triangle("yellow", True, 7, 8)


circle.describe()
print()
square.describe()
print()
triangle.describe()
