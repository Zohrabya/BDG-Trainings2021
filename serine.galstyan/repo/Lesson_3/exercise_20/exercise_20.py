#!/usr/bin/evn python3

number1 = int(input("Enter 1-st number:"))
number2 = int(input("Enter 2-nd number:"))
number3 = int(input("Enter 3-rd number:"))
number4 = int(input("Enter 4-th number:"))
number5 = int(input("Enter 5-th number:"))
# The largest part
if number1 >= number2:
    largest_from_first_pair = number1
else:
    largest_from_first_pair = number2
if number3 >= number4:
    largest_from_second_pair = number3
else:
    largest_from_second_pair = number4
if largest_from_first_pair >= largest_from_second_pair:
    largest = largest_from_first_pair
else:
    largest = largest_from_second_pair
if number5 >= largest:
    final_largest = number5
else:
    final_largest = largest
print("Largest is", final_largest)

# The smallest part
if number1 <= number2:
    smallest_from_first_pair = number1
else:
    smallest_from_first_pair = number2
if number3 <= number4:
    smallest_from_second_pair = number3
else:
    smallest_from_second_pair = number4
if smallest_from_first_pair <= smallest_from_second_pair:
    smallest = smallest_from_first_pair
else:
    smallest = smallest_from_second_pair
if number5 <= smallest:
    final_smallest = number5
else:
    final_smallest = smallest
print("Smallest is", final_smallest)
