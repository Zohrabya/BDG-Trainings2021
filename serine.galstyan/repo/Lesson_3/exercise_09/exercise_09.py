#!/usr/bin/evn python3

price = int(input("Enter the price of the meal:"))
percent = int(input("Enter the percent:"))
tip = price * percent / 100
total_bill = price + tip
print("Tip amount:", tip, "\nBill(included tip):", total_bill, sep=" ")
