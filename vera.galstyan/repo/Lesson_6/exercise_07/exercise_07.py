#!usr\bin\env python 3

user_number = int(input("Enter a number: "))

list_of_numbers = []
while user_number != 0:
    list_of_numbers.append(user_number)
    user_number = int(input("Enter next number or '0' to print the average: "))

numbers_average = sum(list_of_numbers) / len(list_of_numbers)
print(round(numbers_average2))
