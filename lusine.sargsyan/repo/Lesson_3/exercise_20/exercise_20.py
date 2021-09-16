#!/usr/bin/env python3

number_1 = int(input("Please neter the 1st number: "))
number_2 = int(input("Please neter the 2nd number: "))
number_3 = int(input("Please neter the 3th number: "))
number_4 = int(input("Please neter the 4th number: "))
number_5 = int(input("Please neter the 5th number: "))
smallest = number_1
if number_2 < smallest:
    smallest = number_2
if number_3 < smallest:
    smallest = number_3
if number_4 < smallest:
    smallest = number_4
if number_5 < smallest:
    smallest = number_5 
print("the smallest number is:", smallest)
largest = number_1
if number_2 > largest:
    largest = number_2
if number_3 > largest:
    largest = number_3
if number_4 > largest: 
    largest = number_4
if number_5 > largest:
    largest = number_5
print("The largest number is: ", largest)

