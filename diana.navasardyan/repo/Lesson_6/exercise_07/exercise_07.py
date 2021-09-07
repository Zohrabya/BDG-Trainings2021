#!/usr/bin/env python3

num_1 = int(input(" Please enter a number (Hint:Enter '0' to calculate the average): "))
num_1_list = []

while num_1 != 0:
    num_1_list.append(num_1)
    num_1 = int(input("Please enter another number: "))
num_average = sum(num_1_list) / len(num_1_list)
print(num_average)