foods = []
prices = []
total = 0

while True:
    food = input("Enter a food to buy (q to quit): ")
    if food.lower() == "q":
        break
    else:
        price = float(input(f"Enter a price of {food}: $"))
        foods.append(food)
        prices.append(price)

print("----- Your CART ----")

for food in foods:
    print(food)

for price in prices:
    total += price

print(f"your total is: ${total}")
