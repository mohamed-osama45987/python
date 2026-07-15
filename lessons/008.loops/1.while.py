# while loop syntax is as follows:
# while condition:
#     # code to execute while condition is True
# rest of the code


name = input("What is your name? (or 'q' to quit) ")


while name == "":
    print("You didn't enter a name. Please try again.")
    name = input("What is your name?  (or 'q' to quit) ")

print(f"Hello, {name}!")


# you can also make a quit option for the user to exit the loop by using a break statement

while not name == "q":
    print("You didn't enter a name. Please try again.")
    name = input("What is your name?  (or 'q' to quit) ")

print(f"Hello, {name}!")


age = int(input("What is your age?"))

while age < 0:
    print("age cannot be negative. Please try again.")
    age = int(input("What is your age?"))
print(f"Your age is {age}!")
