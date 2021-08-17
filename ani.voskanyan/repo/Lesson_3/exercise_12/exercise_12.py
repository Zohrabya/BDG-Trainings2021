#!/usr/bin/env python3

container_quantity_less = int(input("Please, enter quantity of drink containers holding one liter and less : "))
container_quantity_more = int(input("Please, enter quantity of drink containers holding more than one liter:  "))
DEPOSIT_1 = 0.10
DEPOSIT_2 = 0.25
total_refund = DEPOSIT_1 * container_quantity_less + DEPOSIT_2 * container_quantity_more
print("Your total refund:", total_refund)
