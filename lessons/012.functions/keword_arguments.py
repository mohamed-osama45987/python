def hello(greeting, title, first, last):
    print(f"{greeting} {title}{first} {last}")


hello("Hello", "Mr.", "John", "Doe")

# you can add indentifiers to our arguments to make it map to the paramter without relying on order
hello("Hello", first="John", title="Mr.", last="Doe")


# just like in print function it have some keyword arguments like end and seprate


nums = (1, 2, 3, 4, 5)

# will print all nums on 1 line wite spaces after each num
for num in nums:
    print(num, end=" ")  # 1 2 3 4 5

print()
#  will print 1-2-3
print("1", "2", "3", sep="-")
