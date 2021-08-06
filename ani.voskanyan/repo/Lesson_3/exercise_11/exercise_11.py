field_length = float(input("Please enter the length of the field: "))
field_width = float(input("Please enter the width of the field: "))
field_square_in_feet = field_length * field_width
field_square_in_acre = 43560 * field_square_in_feet

print(f'The square of the field is {field_square_in_acre} acres')
