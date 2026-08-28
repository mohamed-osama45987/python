# decorator are a function that extend the behaviour of another function without changing the
# base function
# pass the base function as an arugument to this decorator


def add_sprinkles(func):
    # wrapper function are needed as without it
    # decorators will vall the inner function at run time without us callin the base function
    # explicitly like get_ice_cream()
    def wrapper(*args, **kwargs):
        print("You add sprinkles")
        func(*args, **kwargs)

    return wrapper


def add_fudge(func):
    def wrapper(*args, **kwargs):
        print("You add fudge")
        func(*args, **kwargs)

    return wrapper


# you use your decorator as a decorator when you define the base function and you can apply more than 1
@add_sprinkles
@add_fudge
def get_ice_cream(flavor):
    print(f"Here is your {flavor} ice cream")


# do not forget it your base function needs and arguments to be passed in the wrapper function
# of your decorators use *args and **kwargs and pass it to the function
get_ice_cream("Choco")  # with decorators applied
