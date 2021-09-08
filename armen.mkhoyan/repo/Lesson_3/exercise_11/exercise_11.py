#!/usr/bin/env python3

width = float(input("Enter a width of farmer's field in feet: "))
length = float(input("Enter a length of farmer's field in feet: "))
SQUARE_FEET_IN_ACRE = 43560
print("Total area of the field is", round((width * length) / SQUARE_FEET_IN_ACRE, 2), "acre")