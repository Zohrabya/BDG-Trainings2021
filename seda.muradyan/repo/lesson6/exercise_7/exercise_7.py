number = int(input("Enter a number (enter '0' to calculate the average): "))
numberslist = []

while number != 0:
    numberslist.append(number)
    number = int(input("Enter another number"))
else:
    numbers_average = sum(numberslist) / len(numberslist)
    print(f'{numbers_average:.2f}')