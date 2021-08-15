#! /usr/bin/env python3

index1 = 0.10
index2 = 0.25
count = int(input("please enter the count of conteiners: "))
liter = int(input("please enter the litrage of conteiners: "))
if (liter <= 1):
    result = count * index1
else:
    result = count * index2
print ("deposite is: $ {0:1.2f}".format(result))
    

    