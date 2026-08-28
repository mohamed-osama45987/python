# object  = is a bundle of related values called attributes and puch of functions called methods to
# manipulate those attributes
# class = is a blue print on how can we build objects

from car import (
    Car,
)  # make sure that the file contain the class has a lower case name and the calss it self has a higher case name

car1 = Car("BMW", 1992, "red", True)


car1.drive()

car1.stop()
