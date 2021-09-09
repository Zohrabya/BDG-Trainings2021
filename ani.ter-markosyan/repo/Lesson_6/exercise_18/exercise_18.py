#!usr/bin/env python3

list_1 = []
item = int
while item != "":
    item = input("Enter the elements of list: ")
    if item != "":
     list_1.append(int(item))
if len(list_1) >= 0 and list_1 == sorted(list_1) or list_1 == sorted(list_1, reverse = True):
    print("The list is sorted")   
else:
    print ("The list is not sorted")
    