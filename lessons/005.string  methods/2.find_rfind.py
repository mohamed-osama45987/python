# any string value have a built in method called .find that returns the first index of the matched search term in a string abd if not found it will return -1
name = input("Enter your Name: ")

# to get where is the user added his first space
spaceIndex = name.find(" ")

lastSpaceIndex = name.rfind(" ")


print(f"Hello {name}, your first space is at index no {spaceIndex}")


# what if you want the last occurence of a search term you can use the revese find method (rfind)

print(f"Hello {name}, your last space is at index no {lastSpaceIndex}")