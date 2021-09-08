#!/usr/bin/env python3

LESS_DEPOS = 0.10
MORE_DEPOS = 0.25
less_liter = int(input("Please enter the count of conteiners with litrage 1l or less: "))
more_liter = int(input("Please enter the count of conteiners with litrage more than 1l: "))
refund = less_liter * LESS_DEPOS + more_liter * MORE_DEPOS
print("Deposite is: $", round(refund))