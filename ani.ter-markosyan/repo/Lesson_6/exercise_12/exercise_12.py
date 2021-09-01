#!usr/bin/evn python3

list = []
numbers = int
while numbers != "":
    numbers = input("Enter the numbers(blank to exit): ")
    if numbers != "":
        list.append(int(numbers))
for item in list:
    if item < 0:
        print(item)
for item in list:
    if item == 0:
        print(item)
for item in list:
    if item > 0:
        print(item)


       



