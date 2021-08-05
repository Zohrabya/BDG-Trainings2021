#!/usr/bin/env python3

number_1 = int(input("Enter a first number: "))
number_2 = int(input("Enter a second number: "))
number_3 = int(input("Enter a third number: "))

#inputed integers
print("Entered three different numbers: ", number_1, number_2, number_3)

#sum
print("Sum is ", number_1+number_2+number_3)

#average
print("Average is ", (number_1+number_2+number_3)/3)

#product
print("Product is ", number_1*number_2*number_3)

#smallest
if number_1<number_2 and number_1<number_3:
    print("Smallest is ", number_1)
elif number_2<number_1 and number_2<number_3:
    print("Smallest is ", number_2)
elif number_3<number_1 and number_3<number_2:
    print("Smallest is ", number_3)
elif number_1 == number_2 and number_1<number_3 or number_2 <number_3:
    print("Smallest is ", number_1)
elif number_1 == number_3 and number_1<number_2 or number_3<number_2:
    print("Smallest is ", number_1)
elif number_3 == number_2 and number_3<number_1 or number_2 <number_1:
    print("Smallest is ", number_2)

#largest
if number_1>number_2 and number_1>number_3:
    print("Largest is ", number_1)
elif number_2>number_1 and number_2>number_3:
    print("Largest is ", number_2)
elif number_3>number_1 and number_3>number_2:
    print("Largest is ", number_3)
elif number_1 == number_2 and number_1>number_3:
    print("Largest is ", number_1)
elif number_1 == number_3 and number_1>number_2:
    print("Largest is ", number_1)
elif number_3 == number_2 and number_3>number_1:
    print("Largest is ", number_3)