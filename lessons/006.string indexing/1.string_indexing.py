# indexing mean accessing an element of a string using [] (index operator)
# [start:end:step] is the syntax for slicing a string
# -1 mean in reverse order
# leaving a value blank means to take the whole string
# the start is inclusive and the end is exclusive

credit_number = "1234-5678-9012-3456"


credit_number[0]  # get you the first character of the string which is 1
credit_number[-1]  # get you the last character of the string which is 6 you can travers the string in reverse order using negative indexing
credit_number[0:4]  # get you the first 4 characters of the string which is 1234 you can also use credit_number[:4] to get the same result
credit_number[5:9]  # get you the 4 characters starting from index 5 to index 8 which is 5678
credit_number[5:]  # get you the characters starting from index 5 to the end of the string which is 5678-9012-3456 
credit_number[::2]  # get you the characters starting from index 0 with a step of 2 which is 13579246 
credit_number[-4:]  # get you the last 4 characters of the string which is 3456 notice that credit_number[-4:] is not the same as credit_number[-4] as the first one will give you a string while the second one will give you a character 
credit_number[::-1]  # get you the string in reverse order which is 6543-2109-8765-4321

