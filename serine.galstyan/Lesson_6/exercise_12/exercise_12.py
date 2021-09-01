#!/usr/bin/evn python3

collection_of_integers = []
final_list = []
index = 0
entered_integer = input("Enter an integer: (blank to quit): ")
while entered_integer != "":
    collection_of_integers += [entered_integer]
    entered_integer = input("Enter an integer: (blank to quit): ")
    if entered_integer == "":
        break
for element in collection_of_integers:
    if "-" in element:
        final_list += [element]
    else:
        continue
for element in collection_of_integers:
    if int(element) == 0:
        final_list += element
    else:
        continue
for element in collection_of_integers:
    if int(element) > 0:
        final_list += element
    else:
        continue
for element in final_list:
    print(final_list[index], "\n")
    index +=1
