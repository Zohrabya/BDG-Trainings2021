#! /usr/bin/env python3

width = int(input("Enter the width of the box: "))
height = int(input("Enter the height of the box: "))
print("*" * width)
for i in range(height - 2):
    print("*", " " * (width - 2), "*", sep = "")
print("*" * width)