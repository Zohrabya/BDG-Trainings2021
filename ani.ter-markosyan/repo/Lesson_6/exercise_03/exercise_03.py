#!usr/bin/evn python3

rows = int(input("Enter the number of rows: "))
for i in range(rows):
    print("*" * (i + 1) + " " * (rows - 1 - i))