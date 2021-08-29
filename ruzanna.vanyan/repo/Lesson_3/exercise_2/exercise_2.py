#!/usr/bin/env python3

width = int(input("Enter a width of shape"))
height = int(input("Enter a height of shape"))
print("*" * width)
for i in range(height - 2):
    print("*", " " * (width - 2), "*", sep = "")
print("*" * width)
