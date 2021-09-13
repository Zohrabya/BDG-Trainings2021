#!/usr/bin/evn python3

total = 0
index = 0
collection = ""
print("Enter the collection of values: ")
while 1 == 1:
    entered_value = input()
    if entered_value == "0":
        break
    collection += entered_value
for element in collection:
    total += int(collection[index])
    index += 1
average = total / len(collection)
print("The average of entered values is: ", round(average, 3))
