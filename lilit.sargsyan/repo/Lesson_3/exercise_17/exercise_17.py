num_1 = int(input('Input the first integer: '))
num_2 = int(input('Input the second integer: '))
num_3 = int(input('Input the third integer: '))
sum_of_numbers = num_1 + num_2 + num_3
print('Sum is', float(sum_of_numbers))
average_of_numbers = sum_of_numbers / 3
print('Average is', int(average_of_numbers))
product_of_numbers = num_1 * num_2 * num_3
print('Product is', float(product_of_numbers))
if (num_1 > num_2) and (num_1 > num_3) or (num_1 < num_2) and (num_1 < num_3):
    print('Largest is', num_1) or ('Smallest is', num_1)
elif (num_2 > num_1) and (num_2 > num_3) or (num_2 < num_1) and (num_2 < num_3):
    print('Largest is', num_2) or ('Smallest is', num_2)
else:
    print('Largest is', num_3) or ('Smallest is', num_3)