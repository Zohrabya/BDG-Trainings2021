#!/usr/bin/env python3

barer = list()
bar = input("Enter the word: ")
while bar != "":
    if bar not in barer:
        barer.append(bar)
    bar = input("Enter the word: ")
for item in barer:
    print(item)