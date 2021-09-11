#!/usr/bin/env python3
#Order amount
cost = float(input("Enter the cost of the meal: "))

#tax is 6% 
tax_amount = cost * 6/100

#Tip is 18%, without the tax.
tip_amount = cost * 18/100

print("Tax: ","$", round(tax_amount,2)," (Tip is 6%)" )
print("Tip: ","$", round(tip_amount, 2)," (Tip is 18%, without the tax)")
print("Total cost is: ", "$", round(cost + tax_amount + tip_amount, 2))