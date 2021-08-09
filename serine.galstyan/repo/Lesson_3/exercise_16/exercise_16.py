#!/usr/bin/evn python3

first_num = int(input("Enter first integer:"))
second_num = int(input("Enter second integer:"))
if first_num > second_num:
    print(first_num, "is larger", sep=" ")
elif first_num == second_num:
    print("These numbers are equal.")
else:
    print(second_num, "is larger", sep=" ")
