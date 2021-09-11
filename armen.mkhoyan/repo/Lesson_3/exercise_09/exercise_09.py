#!/usr/bin/env python3

price = float(input("Enter a price: "))
tip_perecent = float(input("Enter a tip percent: "))

tip_amount = price * tip_perecent * 0.01

print("Tip Amount: ", tip_amount,"\nTotal Bill: ", tip_amount+price)