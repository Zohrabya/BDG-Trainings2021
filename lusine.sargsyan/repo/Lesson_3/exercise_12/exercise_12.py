#! /usr/bin/env python3


deposite_1 = 0.10
deposite_2 = 0.25
count1 = int(input("please enter the count of conteiners with litrage 1l or less: "))
count2 = int(input("please enter the count of conteiners with litrage more than 1l: "))

print ("Deposite is: $ {0:1.2f}".format(count1 * deposite_1 + count2 * deposite_2))
