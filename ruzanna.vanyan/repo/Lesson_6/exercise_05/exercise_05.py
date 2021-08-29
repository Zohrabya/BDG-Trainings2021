#!/usr/bin/env python3

height = int(input("Enter the height of the diamond: "))
for i in range(height):
    print(" " * (height - i - 1) + "* " * (i + 1))
for j in range(height-1, 0, -1):
    print(" " * (height - j) + "* " * (j))

