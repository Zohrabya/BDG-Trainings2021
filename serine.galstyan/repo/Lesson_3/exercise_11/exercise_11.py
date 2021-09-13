#!/usr/bin/env python3

width = float(input("Enter the width(in feet): "))
length = float(input("Enter the length(in feet): "))
feets_in_an_acre = 43560
field_area = width * length / feets_in_an_acre
print("The area of the field is", round(field_area, 4), "acres.", sep=" ")
