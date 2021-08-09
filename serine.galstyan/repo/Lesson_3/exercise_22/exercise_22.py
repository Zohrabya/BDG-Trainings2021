#!/usr/bin/evn python3

first_number = int(input("Enter the first number:"))
second_number = int(input("Enter the second number:"))
if first_number % second_number == 0:
    print(first_number, "is a multiple of", second_number, sep=" ")
else:
    print(first_number, "is NOT a multiple of", second_number, sep=" ")
