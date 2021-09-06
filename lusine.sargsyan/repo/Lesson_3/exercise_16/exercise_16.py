#!/usr/bin/env python3

first_number = int(input("Enter the first number: "))
second_number = int(input("Enter the second number: "))
if first_number > second_number:
    print(first_number, "is larger.")
elif first_number < second_number:
    print(second_number, "is larger.")
else: 
    print("The numbers are equal.")