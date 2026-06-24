
unit = input("Is the temp is Celsius or Fahrenheit (C/F): ")

temp = float(input("Enter the Temp: "))



# the math equation is ((temp x 9)/5 ) + 32 to convert from Celsius to Fahrenheit

if unit == "C":
    temp = (temp * 9 ) / 5 + 32
    print (f"Your Temp is {round(temp,1)} in Fahrenheit")
elif unit == "F":
    temp = ( temp - 32) * 5 / 9
    print (f"Your Temp is {round(temp,1)} in Celsius")
else:
    print(f"{unit} was not valid")