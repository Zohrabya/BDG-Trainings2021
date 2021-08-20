#! /usr/bin/env python3

meal_price = int(input("Enter the price of the meal: "))
meal_tip = int(input("Enter the desired tip in percents: "))

To_be_paid = meal_price + meal_price * meal_tip / 100

print("Tip: ", meal_tip, "%", "\nTo be paid: ", To_be_paid, "USD")
