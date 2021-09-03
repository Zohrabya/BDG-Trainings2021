#!usr/bin/evn python3

number1, number2, number3 = (input("Input three different integers: ").split())
sum = int(number1) + int (number2) + int(number3)
average = round(int (number1) + int(number2) + int(number3) / 3, 2)
product = int(number1) * int(number2) * int(number3)
if number1 > number2 and number1 > number3:
    if number2 < number3:
        largest = number1
        smallest = number2
    else:
        smallest = number3
elif number2 > number1 and number2 > number3:
    if number1 < number3:
        largest = number2
        smallest = number1
    else:
        smallest = number3
else:
    largest = number3
    if number1 < number2:
        smallest = number1
    else:
        smallest = number2
print("Sum is", sum), print("Average is", average), print("Product is", product), print("Smallest is", smallest), print("Largest is", largest)