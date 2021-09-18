#!usr/bin/env python3

negative_numbers = []
positive_numbers = []
zero_list = []

number_input = input("Enter a number: ")

while number_input != '':
    if int(number_input) < 0:
        negative_numbers.append(number_input)
        number_input = input("Enter a number: ")
    elif int(number_input) > 0:
        positive_numbers.append(number_input)
        number_input = input("Enter a number: ")
    else:
        zero_list.append(number_input)
        number_input = input("Enter a number: ")
else:
    print(negative_numbers + zero_list + positive_numbers)
