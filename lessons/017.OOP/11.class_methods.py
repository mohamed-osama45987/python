# Class methods are methods that allow opeartions relateed to teh class it self not its object
# it takes the (cls) as first paramter which repersent a class


# insance methods are best used if you want to make operations on the objects resulted from a class
# Static methods are best used to make util function that does not need access to class data
# Class methods are best uset to operate on class level data or require access to class data


class Student:
    count = 0
    total_gpa = 0

    def __init__(self, name, gpa):
        self.name = name
        self.gpa = gpa
        Student.count += 1
        Student.total_gpa += gpa

    # instance method
    def get_info(self):
        return f"{self.name} - {self.gpa}"

    # class method
    @classmethod
    def get_count(cls):
        return f"the count of students are {cls.count}"

    @classmethod
    def get_average_gpa(cls):
        return (
            0 if cls.count == 0 else f"The average gpa is {cls.total_gpa/cls.count:.2f}"
        )


print(Student.get_count())  # 0

student1 = Student("Spongebob", 3.2)
student2 = Student("Partick", 2.0)
student3 = Student("Sandy", 4.0)

print(Student.get_count())  # 3

print(Student.get_average_gpa())
