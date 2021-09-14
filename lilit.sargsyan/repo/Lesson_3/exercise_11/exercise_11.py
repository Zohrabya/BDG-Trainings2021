lenght_of_field = float(input('Enter the lenght of a farmer field in feet:' ))
width_of_field = float(input('Enter the width of a farmer in feet:' ))
one_acre = 43.560
area_of_the_field = lenght_of_field * width_of_field
acres_together =  area_of_the_field / one_acre
print('The total area of the field in acres is: ', acres_together, 'acre')