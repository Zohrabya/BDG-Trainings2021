#!usr/bin/evn python3

rows = int(input("Enter the number of rows of the box: "))
columns = int(input("Enter the number of columns of the box: "))
for i in range(rows):
    for j in range(columns):
        print("*", end= "")
    print()
