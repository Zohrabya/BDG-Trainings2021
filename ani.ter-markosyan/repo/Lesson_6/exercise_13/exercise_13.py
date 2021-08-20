#!usr/bin/evn python3

integer_1 = int(input("Enter an integer: "))
for i in range(1, integer_1):
    if integer_1 % i == 0:
        print (i)