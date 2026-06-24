

weight = float(input("Please enter your weight: "))
unit = input("Kilograms or Pounds ? (K/L): ")


constant = 2.205 # as 1kg is equal to 2.205 pound
printedUnit = "Kg."


if unit == "K":
    weight = weight * constant # converting weight to pounds
    printedUnit = "Lbs."
    print(f"Your Weight is: {round(weight,1)} {printedUnit}")
elif unit == "L":
    weight = weight / constant
    print(f"Your Weight is: {round(weight,1)} {printedUnit}")
else :
    print(f"{unit} was not valid")


