# lists are an array of similar values. values are index ordered and changable and dups are ok


fruits = ["apple", "orange", "banana", "coconut"]

print(fruits)

# you can use [] to access element same like in string indexing

print(fruits[0])  # apple

# iterate over the fruits array
for fruit in fruits:
    print(fruit)


# there is a lot of built in methods

# print(help(fruits))


# length
print(len(fruits))

# find if value in list
print("apple" in fruits)  # true
print("pineapple" in fruits)  # false


# you can change values using indexs
fruits[0] = "pinapple"
print(fruits)  # [pinapple, ...]


# append and remove
# append adds value at the end of an array
# remove removes the value from the end of an array

fruits.append("beach")
print(fruits)  # [..., beach]

fruits.remove("beach")
print(fruits)  # [...] beach is removed as it was the last element


# insert a value at a given index
fruits.insert(0, "grapes")
print(fruits)  # ['grapes', 'pinapple', 'orange', 'banana', 'coconut']


# sort allow you to sort accendegly or in alphabetical order
fruits.sort()
print(fruits)  # ['banana', 'coconut', 'grapes', 'orange', 'pinapple']

# to reverse an array based on ther index

fruits.reverse()
print(fruits)  # ['pinapple', 'orange', 'grapes', 'coconut', 'banana']


# index of a value will error if value not found
print(fruits.index("pinapple"))  # 0


# count to count total number of occurnce of an element in a list
print(fruits.count("banana"))  # 1

# clear a list
fruits.clear()
print(fruits)  # []
