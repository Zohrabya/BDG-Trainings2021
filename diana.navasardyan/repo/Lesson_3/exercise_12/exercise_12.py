#!/usr/bin/env python3

number_1 = float(input("Enter quantity of drink containers holding one liter and less: "))
number_2 = float(input("Enter quantity of drink containers holding more than one liter: "))

refundable_amount = round(number_1 * 0.10, 2) + round(number_2 * 0.25)
    
print("Your refundable amount:", refundable_amount, "$")
