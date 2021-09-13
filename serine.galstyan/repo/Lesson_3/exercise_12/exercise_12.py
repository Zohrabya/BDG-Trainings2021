#!/usr/bin/env python3

liter_or_less = int(input("Enter the number of containers that holding 1 liter or less: "))
more_than_liter = int(input("Enter the number of containers that holding more than 1 liter: "))
lightweight_container_deposit = 0.10
heavy_container_deposit = 0.25
total = (lightweight_container_deposit * liter_or_less) + (heavy_container_deposit * more_than_liter)
print("The refund for returning containers is $" + str(round(total, 2)) + ".")
