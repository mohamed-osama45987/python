# calulating the hypothones of right angle triangle ( hyp = root of a^2 + b*2 )
import math

a = float(input("enter the first side length: "));
b = float(input("enter the second side length: "));

hyp = math.sqrt(math.pow(a,2) + math.pow(b,2));

print(f"The hypotones is {hyp}")