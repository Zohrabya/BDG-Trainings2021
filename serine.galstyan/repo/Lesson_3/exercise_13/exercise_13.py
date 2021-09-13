#!/usr/bin/env python3

meal_cost = int(input("Enter the cost of the meal: "))
tax_rate = 0.09
tip = 0.18
tax_amount = meal_cost * tax_rate
tip_amount = meal_cost * tip
grand_total = meal_cost + tax_amount + tip_amount
print("The tax amount is: ", round(tax_amount, 2), "\nThe tip amount is: ", round(tip_amount, 2), 
"\nThe total is: ", round(grand_total, 2), sep=" ")
