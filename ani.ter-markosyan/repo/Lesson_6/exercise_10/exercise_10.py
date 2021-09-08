#!usr/bin/env python3

from math import sqrt

perimeter = 0
x_coordinate = float(input("Enter x part of the coordinate: "))
y_coordinate = float(input("Enter y part of the coordinate: "))
x = x_coordinate
y = y_coordinate
x_coordinate1 = input("Enter x part of the coordinate(blank to quit: ")
while x_coordinate1 != "":
    x_coordinate2 = float(x_coordinate1)
    y_coordinate2 = float(input("Enter y part of the coordinate: "))
    distance = sqrt((x - x_coordinate2) ** 2 + (y - y_coordinate2) ** 2)
    perimeter += distance
    x = x_coordinate2
    y = y_coordinate2
    x_coordinate1 = input("Enter x part of the coordinate(blank to quit): ")
distance = sqrt((x- x_coordinate) ** 2 + (y - y_coordinate) ** 2)
perimeter += distance
print ("The perimeter of the poligon is", perimeter)