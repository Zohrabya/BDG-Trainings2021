#!/usr/bin/env python3

#tax and tip Rates in percentage 
TAXR = 20 
TIPR = 18 
price = float(input("Please neter the price of the meal: "))
tax = price * TAXR / 100
tip = price * TIPR / 100
total = price + tip + tax 
print("Tip: $ {0:1.2f}".format(tip), "\nTax: $ {0:1.2f}".format(tax), "\nTotal amount: $ {0:1.2f}".format(total))