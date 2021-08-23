#!/usr/bin/evn python3

wide = int(input("Enter a Wide: "))
high = int(input("Enter a High: "))

for asterisks in range(0,high):
    if asterisks == 0 or asterisks == high-1:
        print("*" * wide)
    
    else:
        print("*", " " * (wide-4), "*") 