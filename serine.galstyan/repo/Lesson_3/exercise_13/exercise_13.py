#!/usr/bin/evn python3

meal_cost = int(input("Enter the cost of the meal:"))
tax_amount = meal_cost * 9 / 100
tip_amount = meal_cost * 18 / 100
grand_total = meal_cost + tax_amount + tip_amount
print("The tax amount is:", round(tax_amount, 2), "\nThe tip amount is:", round(tip_amount, 2), 
"\nThe total is:", round(grand_total, 2), sep=" ")
