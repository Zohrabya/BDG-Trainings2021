#!/usr/bin/env python3

height = int(input("Enter the height of letter A: "))
for i in range(0, height):
    if i == 0:
        print(" " * (height -1 -i) + "*")
    elif height % 2 == 0 and i == (height // 2):
        print((height - 1 - i) * " " + (height + 1) * "*")
    elif height % 2 != 0 and i == (height // 2):
        print((height - 1 - i) * " " + (height) * "*")
    else:    
        print(" " * (height - i - 1) + "*" + ((2 * i) - 1) * " " + "*")
   