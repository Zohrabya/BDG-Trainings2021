#!/usr/bin/env python3

meal_cost = float(input("Please, enter the cost of the meal: "))
TAX_PERCENTAGE = 0.20
cost_tax = meal_cost * TAX_PERCENTAGE
TIP_PERCENTAGE = 0.18
tip = meal_cost * TIP_PERCENTAGE
total_cost = meal_cost + cost_tax + tip

print(f'Tax: {cost_tax:.2f}$. Tip: {tip:.2f}. Total: {total_cost:.2f}$')
