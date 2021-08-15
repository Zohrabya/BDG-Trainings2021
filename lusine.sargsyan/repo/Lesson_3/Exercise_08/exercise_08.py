#!/usr/bin /env python3

list1 = []
list1.append(int(input("enter a number1: ")))
list1.append(int(input("enter a number2: ")))
list1.append(int(input("enter a number3: ")))

total = sum(list1)
average = total / len(list1)

print("Total: ", total, "\nAverage: ", average)