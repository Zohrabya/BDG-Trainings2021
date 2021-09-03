#!usr/bin/env python3 

user_number  = float(input("Please enter the number: "))
total = 0
count = 0
while user_number != 0: 
    total += user_number
    count += 1
    user_number  = float(input("please enter the number: "))
print("Average is: {0:1.4f}".format(total / count))