#!/usr/bin/evn python3

"""
2.	Use a for loop to print a box like the one below. Allow the user to specify how wide and how
high the box should be.
"""

wide = int(input("Enter a Wide: "))
high = int(input("Enter a High: "))

for asterisks in range(0,high):
    if asterisks == 0 or asterisks == high-1:
        print("*" * wide)
    
    else:
        print("*", " " * (wide-4), "*") 