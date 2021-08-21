#! /usr/ bin/env python3

user_integer_1 = int(input("Enter the first integer: "))
user_integer_2 = int(input("Enter the second integer: "))

if user_integer_1 % user_integer_2 == 0: 
    print("The first integer is multiple of the second integer.")
else: 
    print("The first integer is NOT multiple of the second integer.")
