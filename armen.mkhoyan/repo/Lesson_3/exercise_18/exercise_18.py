#!/usr/bin/env python3

radius = int(input("Enter radius: "))

#diameter
diameter = 2 * radius
print("Diameter is: ", diameter)

#circumference (π=3.14159)
P_CONSTANT = 3.14159
circumference = 2 * P_CONSTANT * radius
print("Circumference is: ", circumference)

#area (π=3.14159)
area = P_CONSTANT * radius * radius
print("Area is: ", area)
