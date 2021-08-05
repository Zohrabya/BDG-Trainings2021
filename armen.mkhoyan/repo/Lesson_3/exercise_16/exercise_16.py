#!/usr/bin/env python3

first_number = int(input("Enter first integer number: "))
second_number = int(input("Enter second integer number: "))

if first_number > second_number:
    print(first_number," is larger.")
elif second_number > first_number:
    print(second_number, " is larger")
else:
    print("These numbers are equal.")