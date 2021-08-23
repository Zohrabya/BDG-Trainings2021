#! /usr/bin/env python3

numbers_list = []

number_input = input("Enter number: ")
while number_input != "":
    numbers_list.append(int(number_input))
    number_input = input("Enter another number: ")

if len(numbers_list) > 1 and numbers_list == sorted(numbers_list):
    print("Numbers are sorted in ascending order")
elif len(numbers_list) > 1 and numbers_list == sorted(numbers_list, reverse = True):
    print("Numbers are sorted in descending order")
elif len(numbers_list) == 0:
    print("You haven't entered any number")
elif len(numbers_list) == 1:
    print("You entered only one number")
else:
    print("Numbers aren't sorted")
