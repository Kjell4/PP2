import math

n = int(input("Input number of sides: "))
l = int(input("Input the length of a side: "))

print("The area of the polygon is: ",int((n*l*l)/(4*math.tan(math.pi/n))))