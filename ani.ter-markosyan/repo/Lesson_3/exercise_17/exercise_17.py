#!usr/bin/evn python3

number1 = int(input("Input the first number: "))
number2 = int(input("Input second number: "))
number3 = int(input("input third number: "))
print("Input three different integers:", number1, number2, number3)
sum = number1 + number2 + number3
average = round(number1 + number2 + number3 / 3, 2)
product = number1 * number2 * number3
if number1 > number2 and number1 > number3:
    largest = number1
elif number2 > number1 and number2 > number3:
    largest = number2
else:
    largest = number3
if number1 < number2 and number1 < number3:
    smallest = number1
elif number2 < number1 and number2 < number3:
    smallest = number2
else:
    smallest = number3
print("Sum is", sum), print("Average is", average), print("Product is", product), print("Smallest is", smallest), print("Largest is", largest)