# they are a key value pair data structure they are 
# ordered by insetion in new python 3.7 and above
# and you can not duplicate items in it


capitals = {
    "USA": "Washingtion DC",
    "EGYPT": "Cairo",
    "India": "New Delhi",
    "China": "Beijing",
    "Russia": "Moscow",
}


# (.get) to get values form dict will return None if key is not defined
print(capitals.get("EGYPT"))  # Cairo

if capitals.get("Japan"):
    print("Exists")
else:
    print(
        "That capital does not exist"
    )  # this will be printed as Japan is not in the dict


# (.update) to change the value associated with a key or add new value to the dict

capitals.update({"Germany": "Berlin"})  # adding new value

print(capitals)  # {..., 'Germany': 'Berlin'}

capitals.update({"EGYPT": "New adminstrative capita"})

print(capitals)  # {.. 'EGYPT': 'New adminstrative capita', ...}

# (.pop) to delete a item from a dict

capitals.pop("USA")

print(
    capitals
)  # USA will be removed {'EGYPT': 'New adminstrative capita', 'India': 'New Delhi', 'China': 'Beijing', 'Russia': 'Moscow', 'Germany': 'Berlin'}


# (.popitem) remove the latest value inserted (last) value in the dict
capitals.popitem()

print(
    capitals
)  # {'EGYPT': 'New adminstrative capita', 'India': 'New Delhi', 'China': 'Beijing', 'Russia': 'Moscow'}


# (.keys) to get all the keys in the dict retuns a list

print(capitals.keys())  # ['EGYPT', 'India', 'China', 'Russia']

# (.values) to get all values returns a list
print(
    capitals.values()
)  # ['New adminstrative capita', 'New Delhi', 'Beijing', 'Moscow']

# (.items) returs a list where each value pair is a tupule

print(
    capitals.items()
)  # [('EGYPT', 'New adminstrative capita'), ('India', 'New Delhi'), ('China', 'Beijing'), ('Russia', 'Moscow')]

# you can loop over dict like this 
for key, value in capitals.items():
    print(f"{key}:{value}")

# (.clear) complete empty the dict

capitals.clear()

print(capitals)  # {}
