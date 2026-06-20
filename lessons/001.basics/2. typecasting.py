# typeCasting: how to convert a varable from one type to another

name ="mohamed"
age =25
gpa=3.5
is_student= True


# you can use type() to get the type of the var
print(type(gpa))

# you can use the following functions int(), float(), str(), bool() 
gpa = int(gpa) # convert float to int
print(type(gpa))
print(gpa) # when you convert float to int it will remove the decimal part


strGpa = str(gpa)

print(f"the value is {strGpa} and the type is {type(strGpa)}")
