# 11
width_field = float(input("Enter the width of the field: " ))
length_field = float(input("Enter the length of the field: " ))
ONE_ACRE = 43560
area_of_the_field = width_field * length_field
total_acres = area_of_the_field / ONE_ACRE
print(total_acres,"acre")