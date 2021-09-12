#!/usr/bin/env python3
wide = int(input("Please, input wide of the box: "))
i = 1
while i < wide + 1:
    print(wide*' ', '*'*i)
    wide = wide - 1
    i=i+2
print (wide * ' ', (wide+2)*'*')
i = wide
while i >=1:
    print((wide+1)*' ','*'*i)
    wide = wide + 1
    i = i - 2