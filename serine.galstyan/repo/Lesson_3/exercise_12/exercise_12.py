#!/usr/bin/evn python3

liter_or_less = int(input("Enter the number of containers that holding 1 liter or less:"))
more_than_liter = int(input("Enter the number of containers that holding more than 1 liter:"))
total = (0.10 * liter_or_less) + (0.25 * more_than_liter)
final = round(total, 2)
print("The refund for returning containers is $" + str(final) + ".")
