# we can use the input() function to accept the user input from the stdIn returns a string

name = input("What is your name ?")

# all user inputs are strings so we need to cast it so the addition can be performed at the next line
age = int(input("What is your age ?"))

age += 1

print(f"Hello MR.{name}, you are {age} years old.")


