#!/usr/bin/env python3

entered_numbers = input("Input three different integers: ")
lst = entered_numbers.split(" ")
first_num = int(lst[0])
second_num = int(lst[1])
third_num = int(lst[2])
print("Sum is", first_num + second_num + third_num)
print("Average is", round((first_num + second_num + third_num) / 3, 2))
print("Product is", first_num * second_num * third_num)
smallest = first_num
if second_num < smallest:
    smallest = second_num
if third_num < smallest:
    smallest = third_num
print("Smallest is", smallest)
# the largest part
largest = first_num
if second_num > largest:
    largest = second_num
if third_num > largest:
    largest = third_num
print("Largest is", largest)
