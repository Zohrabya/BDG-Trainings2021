#!usr/bin/env python3

#1
number1, number2, number3, number4, number5 = map(int,input("Enter five different numbers: ").split())
#2
largest = max(number1, number2, number3, number4, number5)
smallest = min(number1, number2, number3, number4, number5)
#3
print("Largest is", largest,"Smallest is", smallest)