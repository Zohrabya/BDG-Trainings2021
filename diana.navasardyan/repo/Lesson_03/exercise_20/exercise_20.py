#!/usr/bin/env python3

number1, number2, number3, number4, number5 = input("Enter a five integers: ")

#largest
largest = number1
if number3 < number2 > number4 and number1 < number2 > number5:
    largest = number2
if number4 < number3 > number5 and number3 > number2:
    largest = number3
if number3 < number4 > number5 and number4 > number2:
    largest = number4
if number3 < number5 > number4 and number5 > number2:
    largest = number5

#smallest
smallest = number1
if number1 > number2 < number4 and number4 > number2 < number5:
    smallest = number2
if number4 > number3 < number2 and number4 > number3 < number5:
    smallest = number3
if number2 > number4 < number3 and number4 < number5:
    smallest = number4
if number2 > number5 < number3 and number5 < number4:
    smallest = number5
print(f"The largest number is {largest}: \nThe smallest number is {smallest}: ")