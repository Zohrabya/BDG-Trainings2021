#!/usr/bin/env python3

liter_or_less = int(input("Enter the number of containers that holding 1 liter or less: "))
more_than_liter = int(input("Enter the number of containers that holding more than 1 liter: "))
LIGHTWEIGHT_CONTAINER_DEPOSIT = 0.10
HEAVY_CONTAINER_DEPOSIT = 0.25
total = (LIGHTWEIGHT_CONTAINER_DEPOSIT * liter_or_less) + (HEAVY_CONTAINER_DEPOSIT * more_than_liter)
print("The refund for returning containers is $" + str(round(total, 2)) + ".")
