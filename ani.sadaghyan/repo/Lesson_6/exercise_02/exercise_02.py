#!/usr/bin/env python3

togh = int(input("Enter the number of togh: "))
qanak = int(input("Enter the number of qanak: "))
for i in range(togh):
    if i == 0 or i == togh -1:
        print("*" * qanak)
    else:
        print("*", " " * (qanak -4), "*")