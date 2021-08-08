number1, number2, number3 = map(int,input("Input three different numbers: ").split())
sum = number1 + number2 + number3
average = (number1 + number2 + number3) / 3
product = number1 * number2 * number3
if (number1 > number2) and (number1 > number3):
    largest = number1
elif (number2 > number1) and (number2 > number3):
    largest = number2
else:
    largest = number3
if (number1 < number2) and (number1 < number3):
    smallest = number1
elif (number2 < number1) and (number2 < number3):
    smallest = number2
else:
    smallest = number3
print("Sum is",sum),print("Average is",average),print("Product is",product),print("Smallest is", smallest),print("Largest is",largest)
