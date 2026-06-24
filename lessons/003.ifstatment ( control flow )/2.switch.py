

age = int(input("Please Enter your age ?"))

match age:
    case age if age > 18:
        print("you are allowed to vote")
    case 18: 
        print("you have one more year to wait")
    case age if age < 0 :
        print("you have not born yet!!!")
    case _ : # in case of less than 18
         print("You are not allowed to vote")


