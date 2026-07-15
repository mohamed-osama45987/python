# for loop is good when you know how many times you want to loop through a block of code. The syntax is as follows:
# for variable in iterable:
#    # code to execute for each item in the iterable

for i in range(1, 11):
    print(f"This is iteration number {i}")
print("------------------------------------------------------")


# if you want to count backwards you can use the reversed() function to reverse the iterable. The syntax is as follows:
for i in reversed(range(1, 11)):
    print(f"This is reverse iteration number {i}")
print("------------------------------------------------------")


# range have a third parameter which is the step value. The syntax is as follows:
for i in range(1, 11, 2):
    print(f"This is iteration number {i} with a step value of 2")


# you can alos iterate through a string using a for loop. The syntax is as follows:
name = "John Doe"
for letter in name:
    print(f"This is letter {letter} in the name {name}")

print("------------------------------------------------------")


# you can use continue statement to skip the current iteration and move to the next iteration. The syntax is as follows:
for i in range(1, 11):
    if i == 5:
        print("Skipping iteration number 5")
        continue
    print(f"This is iteration number {i}")

# you can use break statement to exit the loop. The syntax is as follows:
print("------------------------------------------------------")
for i in range(1, 11):
    if i == 5:
        print("Exiting the loop at iteration number 5")
        break
    print(f"This is iteration number {i}")
