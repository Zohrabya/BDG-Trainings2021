#!/usr/bin/env python3

number1, number2, number3 = input("Enter a three integers: ")

sum_numbers = int(number1) + int(number2) + int(number3)

averege_numbers = int(sum_numbers) / 3

product_numbers = int(number1) * int(number2) * int(number3)
#largest_number
largest = number1
if number2 > number1:
    largest = number2   
if number3 > number2:
    largest = number3

#smallest_number
smallest = number1
if number2 < number1:
    smallest = number2    
if number3 < number2:
    smallest = number3
print(f"Input three deferent integers: {number1} {number2} {number3} \nSum is {sum_numbers} \nAverage is {averege_numbers:.2f} \nProduct is {product_numbers} \nSmallest is {smallest} \nLargest is {largest}")