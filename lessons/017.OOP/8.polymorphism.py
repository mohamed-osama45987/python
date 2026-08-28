# polymorphism  greek word means have many faces or many forms
# there is 2 ways to achive polymorphism through inheritance or duck typing


from abc import ABC, abstractmethod


# abstract methods meaning each child must define his own implementation of it there is no default
# implementation
class Shape:
    @abstractmethod
    def area(self):
        pass


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius


class Square(Shape):
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side**2


class Triangle(Shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area(self):
        return self.base * self.height * 0.5


# a pizza is a circla and a shape 
class Pizza(Circle):
    def __init__(self, radius, topping):
        super().__init__(radius)
        self.topping = topping


# a cirlce is a circle and a shape which means it has 2 forms
shapes = [Circle(4), Square(5), Triangle(6, 7), Pizza(10, "susage")]


for shape in shapes:
    print(shape.area())
