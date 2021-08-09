#!/usr/bin/evn python3

width = float(input("Enter the width(in feet):"))
length = float(input("Enter the length(in feet):"))
field_area = width * length / 43560
print("The area of the field is", round(field_area, 4), "acres.", sep=" ")
