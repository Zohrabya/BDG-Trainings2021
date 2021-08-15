#!/usr/bin/env python3
list1 =list(map(int,input("Input three different integers: ").split()))
print("Sum is:      ", sum(list1))
print("Average is:  ", sum(list1) / len(list1))
print("Product is:  ", list1[0] * list1[1] * list1[2])
print("Smallest is: ",min(list1))
print("Largest is:  ",max(list1))