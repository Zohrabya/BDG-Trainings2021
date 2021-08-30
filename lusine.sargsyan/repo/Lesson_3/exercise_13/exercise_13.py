#! /usr/bin/env python3

price = float(input("Please neter the price of the meal: "))
tax = price * 20 / 100
tip = price * 18 / 100
total = price + tip + tax 

print("tip: $ {0:1.2f}".format(tip), "\ntax: $ {0:1.2f}".format(tax), "\ntotal amount: $ {0:1.2f}".format(total))
