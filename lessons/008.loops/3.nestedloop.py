# nested loops a loop within a loop
# count from 1 to 9 three times
for x in range(3):
    for x in range(1, 10):
        print(x)
    print("--------------")


# to print a grid of whatever symbol

columns = int(input("Enter number of columns: "))
rows = int(input("Enter number of rows: "))
symbol = input("Enter a symbol")

for r in range(rows):
    for c in range(columns):
        print(symbol, end="")
    print()  # to make a new line after the end of each outer loop iteration
