#!usr/bin/evn python3

count = 0 
sum = 0
values = int
while values != 0:
    values = int(input("Enter a value (enter 0 to exit): "))
    sum = sum + values
    count += 1
average = sum / (count-1)
print(f"Average of the values is {average}")