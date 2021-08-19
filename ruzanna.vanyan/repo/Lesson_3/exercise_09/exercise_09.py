#!/usr/bin/env python3

bill = eval(input('Enter the price of the meal: '))
tip = eval(input('Enter the percent tip you want to leave: '))
print('The tip amount is: ', int(bill*tip/100))
print('The total bill amount is: ', int(bill+(bill*tip/100)) )


