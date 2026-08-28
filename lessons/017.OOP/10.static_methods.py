# Static methods are methods that belong to a class instance not to a specific object
# resulted from that class they are generaly used for util functions

# instance methods are normal methods defined inside a class that each object will get a copy of


class Employee:
    def __init__(self, name, position):
        self.name = name
        self.position = position

    # instance method that each object will get a copy of
    def get_info(self):
        return f"{self.name} = {self.position}"

    # static method that belong to the class not it's objects
    # note it does not take self as a argument as it does not have access to object attr
    @staticmethod
    def is_valid_positon(position):
        valid_positions = ["Manager", "Chasier", "Cook", "Janitor"]
        return position in valid_positions


print(
    Employee.is_valid_positon("Cook")
)  # here i called the static method from the class it self


employee1 = Employee("Eugne", "Manager")
employee2 = Employee("Squidward", "Cashier")
employee3 = Employee("SpongBob", "Cook")


print(employee1.get_info())
