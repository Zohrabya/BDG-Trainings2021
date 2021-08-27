#!/usr/bin/env python3
print ("The original price", "\t", "Dicount amount", "\t","The new price")
discount = 60
list_1 = [4.95, 9.95, 14.95, 19.95, 24.95]
for item in (list_1):
    discount_amount = (discount * item) / 100
    new_prices = item - discount_amount
    print (item, 3 * "\t", round(discount_amount, 2), 3 * "\t", round(new_prices, 2))