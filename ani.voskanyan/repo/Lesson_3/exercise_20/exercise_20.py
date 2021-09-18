#!/usr/bin/evn python3

integer_1 = int(input("Enter the first integer: "))
integer_2 = int(input("Enter the second integer: "))
integer_3 = int(input("Enter the third integer: "))
integer_4 = int (input("Enter the fourth integer: "))
integer_5 = int(input("Enter the fifth integer: "))

if integer_1 < integer_2:
     larger_1 = integer_2
     smaller_1 = integer_1
else:
     larger_1 = integer_1
     smaller_1 = integer_2

if integer_3 < integer_4:
     larger_2 = integer_4
     smaller_2 = integer_3
else:
     larger_2 = integer_3
     smaller_2 = integer_4

if larger_1 > larger_2:
     larger_3 = larger_1
else:
     larger_3 = larger_2

if smaller_1 > smaller_2:
     smaller_3 = smaller_1
else:
     smaller_3 = smaller_2

largest_integer = larger_3 if larger_3 > integer_5 else integer_5
smallest_integer = smaller_3 if smaller_3 < integer_5 else integer_5


print(f'Smallest integer is {smallest_integer}. Largest integer is {largest_integer}')
