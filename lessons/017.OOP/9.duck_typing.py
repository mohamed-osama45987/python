# it is the second way to achive polymorphism other than inheritance
# Object can be treated of diffrent types if they have the min requiments for this type
# if it walks like a duck and quacks like a duck then it is a duck


class Animal:
    alive = True


class Dog(Animal):
    def speak(self):
        print("Woof")


class Cat(Animal):
    def speak(self):
        print("Meow")


# here i just changed the method name from honk to speak to fit Animal type
class Car:
    def speak(self):
        print("Honk")


animals = [Dog(), Cat(), Car()]

for animal in animals:
    animal.speak()
