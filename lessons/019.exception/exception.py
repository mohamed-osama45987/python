# how to handle errors in python like try catch blocks in TS
# here we call it try except finally


# a user can type an thing
try:
    number = int(input("Enter a number: "))
    print(1 / number)
# you can chain exception blocks
except ZeroDivisionError:
    print("You can not divide by zero")
except ValueError:
    print("Enter only numebrs please")
# you can catch all exeptions
except Exception:
    print("Somthing went Wrong")
finally:
    print("Do some clean up code here ")
