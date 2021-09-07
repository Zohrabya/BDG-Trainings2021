#!/usr/bin/env python3

SALE = 60
prices_before_sale = [4.95, 9.95, 14.95, 19.95, 24.95]

for i in prices_before_sale:
    print(f'Old price: {i}$. Discount amount: {i * SALE/100:.2f}$. New price: {(i * ((100 - SALE)/100)):.2f}$.')