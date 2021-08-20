#! /usr/bin/env python3

#version1
index1 = 0.10
index2 = 0.25
count = int(input("please enter the count of conteiners: "))
liter = int(input("please enter the litrage of conteiners: "))
if (liter <= 1):
    result = count * index1
else:
    result = count * index2
print ("deposite is: $ {0:1.2f}".format(result))

#version2
index1 = 0.10
index2 = 0.25
count1 = int(input("please enter the count of conteiners having more than 1l litrage: "))
count2 = int(input("please enter the count of conteiners having less than 1l litrage: "))
result = count1 * index2 + count2 * index1

print ("deposite is: $ {0:1.2f}".format(result))




