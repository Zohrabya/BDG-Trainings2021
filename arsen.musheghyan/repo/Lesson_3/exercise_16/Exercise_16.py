#!/usr/bin/env python3
number1 = float(input("Please, enter number1: "))
number2 = float(input("Please, enter number2: "))

if number1 > number2:
  print(number1," is larger ",number2)

if number1 < number2:
  print(number2," is larger ",number1)
elif  number1 == number2:
  print("These numbers are equal.")