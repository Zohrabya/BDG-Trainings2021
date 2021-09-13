#!/usr/bin/env python3

number_1, number_2 , number_3 = input("Input three different integers: ").split(" ")

#sum
sum =int(number_1) + int(number_2) + int(number_3)
print("Sum is ", sum)

#average
print("Average is ", round(sum / 3))

#product
print("Product is ", int(number_1) * int(number_2) * int(number_3))

#smallest
if number_1 < number_2 and number_1 < number_3:
    print("Smallest is ", number_1)
elif number_2 < number_1 and number_2 < number_3:
    print("Smallest is ", number_2)
elif number_3 < number_1 and number_3 < number_2:
    print("Smallest is ", number_3)
elif number_1 == number_2 and number_1 < number_3 or number_2 < number_3:
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