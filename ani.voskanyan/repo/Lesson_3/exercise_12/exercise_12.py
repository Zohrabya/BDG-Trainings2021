#!/usr/bin/env python3
container_quantity_less = int(input("Please, enter quantity of drink containers holding one liter and less : "))
container_quantity_more = int(input("Please, enter quantity of drink containers holding more than one liter:  "))
total_refund = 0.10 * container_quantity_less + 0.25 * container_quantity_more
print("Your total refund:", total_refund)
