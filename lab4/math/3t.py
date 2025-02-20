from math import tan, pi

a=int(input("Input number of sides: "))
b=int(input("Input the length of a side: "))
x=a*(b**2)/(4*tan(pi/a))

print("The area of the polygon is: ", int(x))