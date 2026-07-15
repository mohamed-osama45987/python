# Set is like JS set wich is an array with no dups in it and unordered and immutable but you can add and remove values from it
# if an value is duped it will remove one of them

fruits = {"apple", "orange", "banana", "coconut"}

print(fruits)  # each time will have a new order

fruits.add("pine")

print(fruits)  # {'orange', 'coconut', 'pine', 'banana', 'apple'}

fruits.remove("pine")
print(fruits)  # {'orange', 'coconut', 'banana', 'apple'}

# in to find if the value is in the set or not
print("banana" in fruits)  # True


fruits.clear()
print(fruits)  # set()
