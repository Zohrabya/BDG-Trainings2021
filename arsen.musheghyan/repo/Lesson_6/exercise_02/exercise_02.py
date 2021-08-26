#!/usr/bin/env python3
wide = int(input("Please, input wide of the box: "))
high = int(input("Please, input high of the box: "))
print('*'*wide)
i = 1
for i in range (high):
    print('*',' ' * (wide - 4), '*')
print('*'*wide)