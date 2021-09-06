#!/usr/bin/env python3

DEPOS_1 = 0.10
DEPOS_2 = 0.25
refund_1 = int(input("Please enter the count of conteiners with litrage 1l or less: "))
refund_2 = int(input("Please enter the count of conteiners with litrage more than 1l: "))
refund = refund_1 * DEPOS_1 + refund_2 * DEPOS_2
print ("Deposite is: $", round(refund))