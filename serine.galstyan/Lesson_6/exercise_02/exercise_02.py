#!/usr/bin/evn python3

entered_width = int(input("Enter the width of the box: "))
entered_height = int(input("Enter the height of the box: "))
width = "*" * entered_width
height = "*" * (entered_height - 2)
row = ""
for symbol in width:
    row += "*"
print(row)
for symbol in height:
    print("*" + (entered_width - 2) * " " + "*")
print(row)
