#!usr/bin/env python3

height = int(input("Enter the height of a letter 'A': "))

for i in range(0, height):
    if i == int(height / 2):
        print(("*" * height).center(height * 2, " "))
    elif i == 0: 
        print("*".center(height * 2, " "))
    else: 
        print(("*".ljust(i, " ") + " " + "*".rjust(i, " ")).center(height * 2, " "))
 