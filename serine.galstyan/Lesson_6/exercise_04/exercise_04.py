#!/usr/bin/evn python3

entered_height = int(input("Enter the height of triangle: "))
height = "*" * entered_height
for symbol in height:
    print(entered_height * "*")
    entered_height -= 1
