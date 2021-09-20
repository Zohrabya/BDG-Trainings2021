
#! /usr/bin/env python3 

number1, number2, number3 = input("enter three numbers: ") .split()

print("Sum is: ", int(number1) + int(number2) + int(number3))

print("Average is: ", round((int(number1) + int(number2) + int(number3)) / 3))

print("Product is: ", int(number1) * int(number2) * int(number3))


#the smallest 

if number1 < number2:
    if  number1 < number3: 
        print("The smallest is: ", number1)
elif number2 < number3: 
    print("The smallest is: ", number2)
else: 
    print("The smallest is: ", number3)  

#the largest

if number1 > number2: 
    if number1 > number3: 
        print("The largest is: ", number1)
elif number2 > number3:
    print("The largest is: ", number2)
else: 
    print("The largest is: ", number3)


