#!/usr/bin/env python3

meal_price = float(input("Please enter the price of the meal: "))
percentage_tip = float(input("Please enter a percentage tip: "))

meal_price_percentage_tip = meal_price * percentage_tip / 100
print ("Meal price after applying persent: ", meal_price_percentage_tip)
print ("Total amount: ", meal_price + meal_price_percentage_tip)

