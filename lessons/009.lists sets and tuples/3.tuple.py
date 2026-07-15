# () ordered and unchangable duplicates are okay and faster that a list
# the difference that tuples are not immutable meaning you can not remove or add any thing to it
# once the creation is completed

fruits = ("apple", "orange", "banana", "coconut")


print(len(fruits))  # 4
print("pineapple" in fruits)  # False
print(fruits.index("apple"))  # 0
print(fruits.count("coconut"))  # 1

for fruit in fruits:
    print(fruit)
