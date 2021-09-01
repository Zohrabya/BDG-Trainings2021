#!/usr/bin/evn python3

integer = 1
all_proper_divisors = []
entered_number = int(input("Enter a number: "))
while integer < entered_number:
    if entered_number % integer == 0:
        all_proper_divisors += [integer]
    integer += 1
print("The list of proper divisors is", all_proper_divisors)
