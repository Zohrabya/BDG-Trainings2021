#!/usr/bin/env python3

length_of_field = int(input("Enter the length(in feet): "))
width_of_field = int(input("Enter the width(in feet): "))
ACRES = 43560
area_of_field = (length_of_field + width_of_field) / ACRES
print("The area of the field is", area_of_field )
