#!/usr/bin/env python3
containers_01 = int(input("Please, enter quantity of drink containers holding one liter or less: "))
containers_02 = int(input("Please, enter quantity of drink containers holding more one liters: ")) 
#returns_money = containers_01 * 0,10 + containers_02 * 0.25
print ('Your returns: $','%0.02f' % (containers_01 * 0.10 + containers_02 * 0.25))