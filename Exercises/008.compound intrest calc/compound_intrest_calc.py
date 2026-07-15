# the fromula for to calculate compound intrest is A = P(1 + (r/n))^t
# where A is the final ammount , P is the principal balance the starting balance, r is intrest rate , t number of time period elapcesd

principal = 0
rate = 0
time = 0


while principal <= 0:
    principal = float(input("Enter the principal amount: "))
    if principal <= 0:
        print("Principal can not be less than or equal 0")

while rate <= 0:
    rate = float(input("Enter the intrest rate amount: "))
    if rate <= 0:
        print("Intrest rate can not be less than or equal 0")

while time <= 0:
    time = int(input("Enter the time period in years: "))
    if time <= 0:
        print("Time period can not be less than or equal 0")


total = principal * pow(1 + (rate / 100), time)

print(f"The total amount after {time} years is: {total:.2f}")
