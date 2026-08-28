# @property = Decorator used to define propeties that can be accessed like attributes but
# it gives us the ability to read write and detlet atrributes out of the box
# gives a setter , getter and deleter method


class Rectangle:
    def __init__(self, width, height):
        # add _ before a property to make it protected just by syntax as python does not have private or protected key word
        self._width = width
        self._height = height

    # this to make getter method
    @property
    def width(self):
        return f"{self._width:.1f}cm"

    @property
    def height(self):
        return f"{self._height:.1f}cm"

    # to make setter methods
    @width.setter
    def width(self, new_value):
        if new_value > 0:
            self._width = new_value
        else:
            print("Width must be greater than 0")

    @height.setter
    def height(self, new_value):
        if new_value > 0:
            self._height = new_value
        else:
            print("Height must be greater than 0")

    # to make a deleter
    @width.deleter
    def width(self):
        del self._width
        print("Width has been deleted")

    @height.deleter
    def height(self):
        del self._height
        print("height has been deleted")


rectangle = Rectangle(3, 4)

print(rectangle.width)  # will print the custom string defined on getter methods
print(rectangle.height)

rectangle.width = (
    10  # will error if width is less than 0 as we defined in our setter method
)
rectangle.height = 5


# to delete properties of an obj
del rectangle.width
del rectangle.height
