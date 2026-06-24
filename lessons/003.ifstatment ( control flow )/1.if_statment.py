

age = int(input("Please Enter your age ?"))

# python does not make a new scope for if statments 
if age > 18:
    print("you are allowed to vote")
elif age == 18:
    print("you have one more year to wait")
elif age < 0 :
    print("you have not born yet!!!")
else:
    print("You are not allowed to vote")



