#!usr/bin/evn python3

from math import sqrt 
perimeter = 0
x_coordinate = float(input("Enter the x part of the coordinate: "))
y_coordinate = float(input("Enter the y part of the coordinate: "))
while x_coordinate != "":
    x_coordinate1 = input("Enter the x part of the coordinate:(blank to quit) ")
    y_coordinate1 = float(input("Enter the y part of the coordinate: "))
distance = ((float(x_coordinate1)- x_coordinate)** 2 - (y_coordinate1-y_coordinate)** 2) ** 0,5
perimeter = perimeter + distance
print("Perimeter of polygon is", perimeter)
