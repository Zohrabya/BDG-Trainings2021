#!/usr/bin/env python3

meal_price = float(input("Please enter meal price: ")) 
tax_percentage = 0.20
meal_tax = meal_price * tax_percentage
tip_percentage = 0.18
meal_tip = meal_price * tip_percentage
meal_total_price = meal_price + meal_tax + meal_tip
print("The meal tax is {}\nThe meal tip is {}\nThe grand total of the meal is {}".format(meal_tax,meal_tip,meal_total_price))