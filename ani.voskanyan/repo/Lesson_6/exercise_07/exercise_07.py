#!/usr/bin/env python3

number = int(input("Enter a number (enter '0' to calculate the average): "))
numbers_list = []

while number != 0:
    numbers_list.append(number)
    number = int(input("Enter next number: "))

numbers_average = sum(numbers_list) / len(numbers_list)
print(f'{numbers_average:.2f}')
