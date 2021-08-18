#!usr/bin/evn python3

height = int(input("Enter the height of a diamond: "))
for i in range(0, height):
    if i == 0:
        print (" " * (height - 1) + "*")
    else:
         print (" " * (height - 1 - i) + "*" * (i+1) + "*" * i)
for i in range (0, height-1):
    if i == (height -1):
        print(" " * (i + 1) + "*" * (height - i - 1))
    else:
        print(" " * (i + 1) + "*" * (height - i - 1) + "*" * (height - i - 2))

