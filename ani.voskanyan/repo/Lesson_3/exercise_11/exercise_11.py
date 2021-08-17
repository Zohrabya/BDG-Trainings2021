#!/usr/bin/env python3

field_length = float(input("Please enter the length of the field: "))
field_width = float(input("Please enter the width of the field: "))
FEET_IN_ACRE = 43560
field_square_in_feet = field_length * field_width
field_square_in_acre = field_square_in_feet / FEET_IN_ACRE

print(f'The square of the field is {field_square_in_acre} acres')
