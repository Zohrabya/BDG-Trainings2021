#!/usr/bin/env python3

number1, number2, number3, number4, number5 = input("Enter a five integers: ")

#largest
largest = number1
if number2 > largest:
    largest = number2
if number3 > largest:
    largest = number3
if number4 > largest:
    largest = number4
if number5 > largest:
    largest = number5

#smallest
smallest = number1
if  number2 < smallest:
    smallest = number2
if number3 < smallest:
    smallest = number3
if number4 < smallest:
    smallest = number4
if number5 < smallest:
    smallest = number5
print(f"The largest number is {largest}\nThe smallest number is {smallest}")