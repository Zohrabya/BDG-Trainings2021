#!/usr/bin/env python3

container_quantity_less = int(input("Please, enter quantity of drink containers holding one liter and less: "))
container_quantity_more = int(input("Please, enter quantity of drink containers holding more than one liter:  "))
LESS_DEPOSIT = 0.10
MORE_DEPOSIT = 0.25
total_refund = LESS_DEPOSIT * container_quantity_less + MORE_DEPOSIT * container_quantity_more
print("Your total refund:", total_refund)
