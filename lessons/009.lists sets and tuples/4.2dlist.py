# a 2d list is a list of lists [[],[],[]]
# useful when you need a matrix of data

fruits = ["apple", "oragnes", "banana", "coconut"]
vegtables = ["celery", "carrots", "potatoes"]
meats = ["chicken", "fish", "turkey"]

gorceries = [fruits, vegtables, meats]

print(
    gorceries
)  # [['apple', 'oragnes', 'banana', 'coconut'], ['celery', 'carrots', 'potatoes'], ['chicken', 'fish', 'turkey']]

print(gorceries[0])  # fruits list ["apple", "oragnes", "banana", "coconut"]

print(gorceries[0][0])  # apple [row 0] [column 0]


# nested loops to loop over the entire list
for item in gorceries:
    for food in item:
        print(food)


# you can make a list of tuples [(),(),()]
# or a tuple of tuples ((),(),()) and so on 
