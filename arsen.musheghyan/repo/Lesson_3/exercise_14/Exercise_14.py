#!/usr/bin/env python3
a = int(input("a: "))
x = int(input("x: "))
y = a * (x ** 3) + 7
print (y)
# Value a
if y == a * x * x * x + 7:
    print ("Value a is True")
else:
    print ("Value a is False")
# Value b
if y == a * x * x * (x * 7):
    print ("Value is True")
else:
    print ("Value b is False")
# Value c
if y == (a * x) * x * (x +7):
    print ("Value c is True")
else:
    print ("Value c is False")
# Value d
if y == (a * x) * x * x + 7:
    print ("Value d is True")
else:
    print ("Value d is False")
# Value e    
if y == a * (x * x * x) + 7:
    print ("Value e is True")
else:
    print ("Value e is False")
# Value f    
if y == a * x * (x * x + 7):
    print ("Value f is True")
else:
    print ("Value f is False")