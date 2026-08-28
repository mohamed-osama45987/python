# mutlpiel inheretnce means when one class inhert from 2 or more classes
class Animal:
    # The constructor are inhreted by default
    def __init__(self, name):
        self.name = name

    def eat(self):
        print(f"This {self.name} is eating")

    def sleep(self):
        print(f"This {self.name} is sleeping")


class Prey(Animal):
    def flee(self):
        print(f"This {self.name} is Fleeing")


class Predator(Animal):
    def hunt(self):
        print(f"This {self.name} is hunting")


class Rabbit(Prey):
    pass


class Hawk(Predator):
    pass


# fish can be a eat smaller fish and flee from bigger ones
# so they can muse multiple inheritance
class Fish(Predator, Prey):
    pass


rabbit = Rabbit("Buggs")
hawk = Hawk("Tony")
fish = Fish("Nemo")


fish.flee()  # will work
fish.hunt()  # will work as well

# Multi level inheretnce is when your class inheret from onther class and you inheret from this class all the prorpeties
# he interted it from the first class like here Animal-> prey, preditor -> hawk , fish , rabbit
fish.sleep()
fish.eat()


rabbit.sleep()
