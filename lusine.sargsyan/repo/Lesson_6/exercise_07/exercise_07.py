#!/usr/bin/env python3 

user_number = float(input("Please enter the number: "))
total = 0
count = 0
while user_number != 0: 
    total += user_number
    count += 1
    user_number = float(input("Please enter the number: "))
average = total / count
print("Average is:", round(average, 2))