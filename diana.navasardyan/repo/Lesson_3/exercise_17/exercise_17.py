#!/usr/bin/env python3

number_number = input("Enter a three integers: ")
number1 = str(number_number[0])
number2 = str(number_number[1])
number3 = str(number_number[2])

sum_numbers = int(number1)+ int(number2) + int(number3)

averege_numbers = sum_numbers / 3

product_numbers = int(number1) * int(number2) * int(number3)
#largest_number
if number2 < number1 > number3:
    largest = number1    
elif number1 < number2 > number3:
    largest = number2
else:
    largest = number3
#smallest_number
if number2 > number1 < number3:
    smallest = number1    
elif number1 > number2 < number3:
    smallest = number2
else:
    smallest = number3

print(f"Input three deferent integers: {number1} {number2} {number3} \nSum is {sum_numbers} \nAverage is {averege_numbers:.2f} \nProduct is {product_numbers} \nSmallest is {smallest} \nLargest is {largest}")
