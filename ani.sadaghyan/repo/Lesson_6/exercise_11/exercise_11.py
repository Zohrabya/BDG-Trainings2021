#!/usr/bin/env python3

barer = list()
bar = input("Please enter the word: ")
while bar != "":
    if bar not in barer:
        barer.append(bar)
    bar = input("Please Enter the word: ")
for item in barer:
    print(item)