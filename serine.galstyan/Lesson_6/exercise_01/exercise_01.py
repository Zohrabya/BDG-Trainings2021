#!/usr/bin/evn python3

entered_width = int(input("Enter the width of the box: "))
entered_height = int(input("Enter the height of the box: "))
width = "*" * entered_width
height = "*" * entered_height
row = ""
for x in width:
    row += "*"
for x in height:
    print(row)
