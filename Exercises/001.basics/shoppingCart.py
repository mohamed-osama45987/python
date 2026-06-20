item = input("What item do you want to buy?: ")
price = float(input("What is the price?: "))
quantity = int(input("How many would you like?: "))
total = price * quantity
print(f"Your total will be {total} for {quantity} of {item}")