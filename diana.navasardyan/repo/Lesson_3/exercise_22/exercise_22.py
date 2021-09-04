#!/usr/bin/evn python3

input_number1 = int(input("Please enter the number: "))
input_number2 = int(input("Please enter the number: "))

if input_number1 % input_number2 == 0:
    print(f"{input_number1} is a multiple of {input_number2}")
else:
    print(f" {input_number1} isn't a multiple of {input_number2}")