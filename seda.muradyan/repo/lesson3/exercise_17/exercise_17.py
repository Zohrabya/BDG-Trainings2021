number1, number2, number3 = input("enter three numbers: ") .split()

print("Sum is: ", int(number1) + int(number2) + int(number3))
print("Average is: ", round((int(number1) + int(number2) + int(number3)) / 3))
print("Product is: ", int(number1) * int(number2) * int(number3))

if number1 < number2:
    if  number1 < number3: 
     print("Smallest is: ", number1)
elif number2 < number3: 
    print("Smallest is: ", number2)
else: 
    print("Smallest is: ", number3)  

if number1 > number2: 
    if number1 > number3: 
     print("Largest is: ", number1)
elif number2 > number3:
    print("Largest is: ", number2)
else: 
    print("Largest is: ", number3)