#!usr/bin/env python3

DISCOUNT = 0.6
original_prices = [4.95, 9.95, 14.95, 19.95, 24.95]
print("Old price", "Dicount amount", "New Price", sep = "    ")

for price in original_prices:
    print(price, round(price * DISCOUNT, 2), round(price * (1 - DISCOUNT), 2), sep = " " * 13)