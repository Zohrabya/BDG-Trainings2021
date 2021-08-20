#!usr/bin/env python3

DISCOUNT = 60/100
original_prices = [4.95, 9.95, 14.95, 19.95, 24.95]

for price in original_prices:
    print(f'Old price: {price}$. Discount amount: {price * DISCOUNT:.2f}$. New price: {round(price * (1 - DISCOUNT), 2)}$.')
