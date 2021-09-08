#!/usr/bin/env python3

number_1 = float(input("Enter the number of containers holding: "))

if number_1 <= 1:
    print("Your deposit for containers is", round(number_1 * 0.10, 2), "$")
else:
   print("Your deposit for containers is", round(number_1 * 0.25, 2), "$")

