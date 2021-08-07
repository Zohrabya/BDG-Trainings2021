#! /usr/bin/env python3


price=input("enter the price of the meal:")
tip=input("enter the desired tip in percents:")

price=int(price)
tip=int(tip)

total=price+price*tip/100


print("tip:", tip, "%", "\ntotal price:", total, "USD")