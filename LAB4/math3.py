import math
sides = int(input("Input number of sides:"))
length = int(input("Input the length of a side:"))
area = (sides * length ** 2) / (4 * math.tan(math.pi / sides))
print("he area of the polygon is:", area)