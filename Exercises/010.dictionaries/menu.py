# this is a progam to simulate menus of a resturant

menu = {
    "pizza": 3.00,
    "nachos": 4.50,
    "fries": 2.50,
    "chips": 1.00,
    "pretzel": 3.50,
    "soda": 3.00,
    "lemonade": 4.25,
}


cart = []
total = 0

print("-------------- Menu ---------------")
for key, value in menu.items():
    print(f"{key:10}: ${value:.2f}")
print("-----------------------------------")


while True:
    food = input("Select an item (q to quit): ").lower()
    if food == "q":
        break
    elif menu.get(food) is not None:
        cart.append(food)
    else:
        print(f"{food} is not on the menu")


for food in cart:
    total = total + menu.get(food)
    print(food, end=" ")

print()

print("-------------- Total ---------------")
print(f"Your total is: ${total:.2f}")
