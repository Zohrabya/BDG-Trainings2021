#!/usr/bin/evn python3

print("Input three different integers:")
first_num = int(input())
second_num = int(input())
third_num = int(input())
print("Sum is", first_num + second_num + third_num, sep=" ")
print("Average is", int((first_num + second_num + third_num) / 3), sep=" ")
print("Product is", first_num * second_num * third_num, sep=" ")
# the smallest part
if first_num < second_num:
    if first_num < third_num:
        print("Smallest is", first_num, sep=" ")
    else:
        print("Smallest is", third_num, sep=" ")
else:
    if second_num < third_num:
        print("Smallest is", second_num, sep=" ")
    else:
        print("Smallest is", third_num, sep=" ")
# the largest part
if first_num > second_num:
    if first_num > third_num:
        print("Largest is", first_num, sep=" ")
    else:
        print("Largest is", third_num, sep=" ")
else:
    if second_num > third_num:
        print("Largest is", second_num, sep=" ")
    else:
        print("Largest is", third_num, sep=" ")
