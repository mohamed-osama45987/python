# *args allow you to pass mutliple non-key arguments
# **kwargs allow you to pass mutliple key arguments
# * unpacking operator


# *args gives us a tuple of arguments passed to the function
# you do not have to name it *args they can be *nums
def add(*args):
    print(args)  # (1,2)
    sum = 0
    for arg in args:
        sum += arg

    return sum


print(add(1, 2, 4, 5, 6))


# **kwargs gives you a dictonary {'street': '123 Fake St.', 'city': 'Detroit', 'state': 'MI', 'zip': '54321'}
def print_address(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}:{value}")


print_address(street="123 Fake St.", city="Detroit", state="MI", zip="54321")


# you can use both together but *args must be before **kwargs
def shipping_label(*args, **kwargs):
    for arg in args:
        print(arg, end=" ")
    print()
    for value in kwargs.values():
        print(value, end=" ")


shipping_label(
    "Dr.",
    "John",
    "Doe",
    "III",
    street="123 Fake St.",
    city="Detroit",
    state="MI",
    zip="54321",
)
