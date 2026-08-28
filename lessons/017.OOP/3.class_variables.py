# class variables = aherd amont all instances of a class and defined
# outside the constructor
# ( normal attributes defined inside the constructor are called class variables like class properties in C++)
# Allow you to share data accross all objects created from this class


class Student:
    class_year = 2026
    num_students = 0  # variable to allow us to know how many object was constructed from this class

    def __init__(self, name, age):
        # instance variables
        self.name = name
        self.age = age
        Student.num_students += 1


student1 = Student("Mohamed", 25)
student2 = Student("Ahmed", 20)

print(student1.name)
print(student2.name)

# you can access the class year directly from a class instead of an object instance of this class it is
# best practice
print(Student.class_year)  # 2026
print(student1.class_year)  # 2026


print(Student.num_students)  # 2

student3 = Student("Basma", 21)

print(Student.num_students)  # 3
