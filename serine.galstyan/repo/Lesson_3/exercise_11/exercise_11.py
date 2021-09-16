#!/usr/bin/env python3

width = float(input("Enter the width(in feet): "))
length = float(input("Enter the length(in feet): "))
FEETS_IN_ACRE = 43560
field_area = width * length / FEETS_IN_ACRE
print("The area of the field is", round(field_area, 4), "acres.")
