#!/usr/bin/env python3
#Order amount
cost = float(input("Enter the Cost of the meal: "))

#tax is 6% 
tax_amount = cost * 0.06

#Tip is 18%, without the tax.
tip_amount =cost * 0.18

print("Tax: ","$", tax_amount," (Tip is 6%)" )
print("Tip: ","$", tip_amount," (Tip is 18%, without the tax)")
print("Total Cost Is: ", "$", cost + tax_amount + tip_amount)