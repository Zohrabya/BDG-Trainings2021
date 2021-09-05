number_number = str(input("Enter a five integers: "))
number_1 = int(number_number[0])
number_2 = int(number_number[1])
number_3 = int(number_number[2])
number_4 = int(number_number[3])
number_5 = int(number_number[4])


if number_3 < number_1 > number_2 and number_4 < number_1 > number_5:
    largest = number_1
elif number_1 < number_2> number_3 and number_4 < number_2 > number_5:
    largest= number_2
elif number_1 < number_3 > number_2 and number_4 < number_3 > number_5:
    largest = number_3
elif number_1 < number_4 > number_2 and number_3 < number_4 > number_5:
    largest = number_4
else:
    largest = number_5
print("The largest number is {}:".format(largest))


if number_3 > number_1 < number_2 and number_4 > number_1 < number_5:
    smallest = number_1
elif number_1 > number_2 < number_3 and number_4 > number_2 < number_5:
    smallest = number_2
elif number_1 > number_3 < number_2 and number_4 >number_3 < number_5:
    smallest = number_3
elif number_1 > number_4 < number_2 and number_3 > number_4 < number_5:
    smallest = number_4
else:
    smallest = number_5
print("The smallest number is {}:".format(smallest))

