#!/usr/bin/env python3
meal_price = float(input("Please enter meal price: ")) 
meal_tax = meal_price * 20/100
meal_tip = (meal_price - meal_tax) * 18/100
meal_total_price = meal_price + meal_tax + meal_tip
print("The meal tax is {}\nThe meal tip is {}\nThe grand total of the meal is {}".format(meal_tax,meal_tip,meal_total_price))