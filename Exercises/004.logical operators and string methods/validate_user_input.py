# user can enter a username
# username can not be more than 12 characters
# username can not contain spaces
# username must not have digits

 
username = input("Enter user name : ")

if username.isalpha() != True:
    (
        print("Invalid username as it has spaces in it")
        if username.find(" ") != -1
        else print("Invalid username as it has digits in it")
    )
elif len(username) > 12:
    print("Invalid username as it has more than 12 chars in it")
else:
    print("Valid User name")
