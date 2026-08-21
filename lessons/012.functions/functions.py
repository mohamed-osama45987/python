# use the def keyword to define a function
# default paramter argumennts must follow the non default parameter arguments
def happy_birthday(age, name="you"):
    print(f"Happy birthday to {name}!")
    print(f"you are {age} years old")


happy_birthday(20, "MO")
happy_birthday(10)


# return key word
def sum(num1, num2):
    return num1 + num2

result = sum(1, 2)
print(result)
