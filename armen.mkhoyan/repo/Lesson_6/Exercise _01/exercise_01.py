#!/usr/bin/env python3

"""Use a for loop to print a box like the one below. Allow the user to specify how wide and how
high the box should be. [Hint: print('*' * 10) prints ten asterisks.]
"""

wide = int(input("Enter a Wide: "))
high = int(input("Enter a High: "))

for asterisks in range(0, high):
    print("*" * wide)
