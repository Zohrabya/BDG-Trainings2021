#!/usr/bin/env python3

numbers = int
count = 0 
sum = 0
while numbers != 0:
    numbers = int(input("Enter a value (enter 0 to exit): "))
    sum = sum + numbers
    count += 1
average = sum / (count-1)
print(f"Average of the numbers is {average}")