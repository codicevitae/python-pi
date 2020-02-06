import math
import sys

radiusString = input("Enter the radius: ")

try:
    radius = float(radiusString)
except:
    print("Not a valid radius!")
    sys.exit()

if radius > 0:
    print("Area = ", math.pi * radius * radius)
else:
    print("Radius must be greater than zero!")
