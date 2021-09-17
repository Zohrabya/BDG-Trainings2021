#!/usr/bin/env python3

while True:
    number = int(input("\nPlease enter five-digit number: "))
    number = str(number)
    if len(number) == 5:
        for i in number:
            print(i, end = " " * 2)
        break
    else: 
        print("Integer is not five digit!")