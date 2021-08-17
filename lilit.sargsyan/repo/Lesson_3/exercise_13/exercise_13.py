#!/usr/bin/env python3
cost_meal = float(input('Enter the cost of the meal:'))
tax_rate = 0.20
tax_cost = cost_meal * tax_rate
tip_percent = 0.18
tip = cost_meal * tip_percent
cost_total = cost_meal + tax_cost + tip
print(f'Tax: {tax_cost:120.2f}$. Tip: {tip:.2f}. Total: {cost_total:.2f}$')