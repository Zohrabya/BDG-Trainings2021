#!/usr/bin/env python3

num1 = int(input("Enter a number: "))
num2 = int(input("Enter a number: "))
if num1 % num2 == 0:
    print(num1, "Is a multiple of", num2)
else:
    print(num1, "Isn't multiple of", num2)