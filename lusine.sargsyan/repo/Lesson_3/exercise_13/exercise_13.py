#!/usr/bin/env python3
 
TAX_RATE = 20 
TIP_RATE = 18 
price = float(input("Please neter the price of the meal: "))
tax = price * TAX_RATE / 100
tip = price * TIP_RATE / 100
total = price + tip + tax 
print("Tip: $ {0:1.2f}".format(tip), "\nTax: $ {0:1.2f}".format(tax), "\nTotal amount: $ {0:1.2f}".format(total))