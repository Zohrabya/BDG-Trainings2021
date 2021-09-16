#!usr\bin\env python 3

height = int(input("Enter the height of a diamond: "))
for i in range (1, height):
    print(" " * (height - i) + "*" * (2 * i + 1))
for i in range(-height + 1, 1):
    print (" " * (height + 1 + i) + "*" * (-2 * i - 1))