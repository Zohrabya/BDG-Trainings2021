#1/usr/bin/env python3

percent_1  = float(input("Percent tip: "))
meal_price = float(input("Meal: "))
tip = meal_price * percent_1 / 100
print ("Your price for tip: ", tip)
print ("Total amount: ", meal_price + tip)

