#!/usr/bin/env python3

num = list()
nums = int(input("Enter the number: "))
while num != "":
    num.append(nums)
for item in num:
    if item < 0:
        print(item)
for item in num:
    if item == 0:
        print(item)
for item in num:
    if item > 0:
        print(item)
