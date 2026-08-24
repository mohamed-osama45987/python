# module are lib you can use in your code like npm packages
# there are built in modules in py like random
# you can all additional modules using pip
# your other code in other files that you want to import and export is alos a module
# a simpler explination module is a file contain code that you want to use in your program

# import the hole module
import math

print(math.pi)
# you can use alias
import math as m

print(m.pi)
# import singluar thing within a module
from math import pi

print(pi)

import example_module

print(example_module.pi)
print(example_module.cube(2))
