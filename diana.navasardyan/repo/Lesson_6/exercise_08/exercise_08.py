#!/usr/bin/env python3

SALE = 0.6
prices_before_sale = [4.95, 9.95, 14.95, 19.95, 24.95]

for i in prices_before_sale:
    print(f'Old price: {i}$. Discount amount: {i * SALE:.2f}$. New price: {(i * (1 - SALE)):.2f}$.')