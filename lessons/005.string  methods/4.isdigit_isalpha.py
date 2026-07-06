# you want to see if a string contains an num value you can use isdigit() built in function that will return true or false

num = "4"
print(num.isdigit())  # True

num2 = "Mmmmmm"
print(num2.isdigit())  # False


# isalpha built in method to see if a string contain only alphabetical letters

name="Mohamed"

print(name.isalpha()) # True

name = "Mohamed Osama"

print(name.isalpha()) # False due to the space as it is not a letter 
