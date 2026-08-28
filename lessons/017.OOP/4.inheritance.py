class Animal:
    def __init__(self, name):
        self.name = name
        self.is_alive = True

    def eat(self):
        print(f"{self.name} is eating")

    def sleep(self):
        print(f"{self.name} is sleeping")


# you inheret from another class by adding inhertance list in the class ( list )
class Dog(Animal):
    def speak(self):
        print("WOOF!")


class Cat(Animal):
    # each class can has it's own methods that diffrent from other classes
    def speak(self):
        print("MEOW!")


class Mouse(Animal):
    def speak(self):
        print("SQUEEK!")


dog = Dog("Max")
cat = Cat("Luna")
mouse = Mouse("Jerry")


print(dog.name)
print(dog.is_alive)

dog.eat()
dog.speak()
