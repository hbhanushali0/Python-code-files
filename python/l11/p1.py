# wapp to find area and circumference of circle for which radius is supplied by user
# use math module 

import math

n = float(input("please enter the radius  "))

area = math.pi * math.pow(n, 2)

circumference = 2 * math.pi * n

print("area = ", round(area, 2))
print("circumference = ", round(circumference, 2))

