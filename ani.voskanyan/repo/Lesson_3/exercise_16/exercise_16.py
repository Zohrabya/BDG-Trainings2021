#!/usr/bin/env python3

integer_1 = int(input("Enter the first integer: "))
integer_2 = int(input("Enter the second integer: "))

if integer_1 > integer_2:
    print(integer_1, "is larger")
elif integer_1 < integer_2:
    print(integer_2, "is larger")
else:
    print("These numbers are equal.")
