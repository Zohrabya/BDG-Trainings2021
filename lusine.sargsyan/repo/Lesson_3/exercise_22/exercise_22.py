#!/usr/bin/env python3

number_1 = int(input("Enter the first integer: "))
number_2 = int(input("Enter the second integer: "))

if number_1 % number_2 == 0: 
    print(number_1, "is multiple of the", number_2)
else: 
    print(number_1, "is NOT multiple of", number_2)