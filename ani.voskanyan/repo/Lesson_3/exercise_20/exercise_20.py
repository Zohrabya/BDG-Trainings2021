#!/usr/bin/evn python3

integer_1 = int(input("Enter the first integer: "))
integer_2 = int(input("Enter the second integer: "))
integer_3 = int(input("Enter the third integer: "))
integer_4 = int (input("Enter the fourth integer: "))
integer_5 = int(input("Enter the fifth integer: "))

if integer_1 < integer_2 and integer_1 < integer_3 and integer_1 < integer_4 and integer_1 < integer_5:
    smallest_integer = integer_1
elif integer_2 < integer_1 and integer_2 < integer_3 and integer_2 < integer_4 and integer_2 < integer_5:
     smallest_integer = integer_2
elif integer_3 < integer_1 and integer_3 < integer_2 and integer_3 < integer_4 and integer_3 < integer_5:
     smallest_integer = integer_3
elif integer_4 < integer_1 and integer_4 < integer_3 and integer_4 < integer_2 and integer_4 < integer_5:
     smallest_integer = integer_4
else:
    smallest_integer = integer_5 

if integer_1 > integer_2 and integer_1 > integer_3 and integer_1 > integer_4 and integer_1 > integer_5:
    largest_integer = integer_1
elif integer_2 > integer_1 and integer_2 > integer_3 and integer_2 > integer_4 and integer_2 > integer_5:
     largest_integer = integer_2
elif integer_3 > integer_1 and integer_3 > integer_2 and integer_3 > integer_4 and integer_3 > integer_5:
     largest_integer = integer_3
elif integer_4 > integer_1 and integer_4 > integer_3 and integer_4 > integer_2 and integer_4 > integer_5:
     largest_integer = integer_4
else:
    largest_integer = integer_5 

print(f'Smallest integer is {smallest_integer}. Largest integer is {largest_integer}')
