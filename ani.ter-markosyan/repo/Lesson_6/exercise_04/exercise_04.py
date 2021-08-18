#!usr/bin/evn python3

rows = int(input("Enter the number of rows: "))
for i in range(rows):
        print("*" * (rows - i) + " " * i)
