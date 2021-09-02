#!/usr/bin/evn python3

"""
3.	Use a for loop to print a triangle like the one below. 
Allow the user to specify how high the
triangle should be.
"""

high = int(input("Enter a High: "))

for i in range(0,high+1,+1):
    print("*" * i)

