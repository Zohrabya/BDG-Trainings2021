#!/usr/bin/env python3
costt = float(input("Please, enter the cost of a meal: "))
tax = costt * 1.2 / 100
tip = costt * 1.8 / 100
print ("Tax of meal: ", '%0.02f' % tax)
print ("Tip of meal: ", '%0.02f' % tip)
print ("Total: " '%0.02f' % (costt + tax + tip))