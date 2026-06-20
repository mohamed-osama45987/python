x= 3.4
y= 4 
z= 5


# round () function rounds to the nearest value for 
# 3.14 -> 3 and for 3.5 -> 4 
# if it is less than .5 then the round will be down 
# if it is more than or equal .5 round will be up
# it can be given an additonal argument 
# to tell it to what diciaml point you want to round to
# example round(3.145682154, 2 ) -> 3.14 
result = round(x)
print(result) # 3

# abs () gives you the distance from 0 of a number for example
# -4 will be 4
# essentaily removing the negative sign
tempreature = -25
result = abs(tempreature)
print(result) # 25

# pow () function it makes one number a base then the other is the exponent
#  4 to the power of 3 will be 
result = pow(4,3) # first number is base the second is the power
print(result) # 64

# max () give you the max value in a group of values 
result = max (x,y,z)
print(result) # 5

# min () gives you min value between a group of values
result=min(x,y,z) # 4
print(result)