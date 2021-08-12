num_1 = int(input('Input the first integer:'))
num_2 = int(input('Input the second integer:'))
num_3 = int(input('Input the third integer:'))
sum_of_numbers = num_1 + num_2 + num_3
print('Sum is', int(sum_of_numbers))
average_of_numbers = sum_of_numbers / 3
print('Average is', int(average_of_numbers))
product_of_numbers = num_1 * num_2 * num_3
print('Product is', int(product_of_numbers))
if (num_1 > num_2) and (num_1 > num_3):
    print('Largest is', num_1)
elif (num_2 > num_1) and (num_2 > num_3):
    print('Largest is', num_2)
else:
    print('Largest is', num_3)  
if (num_1 < num_2) and (num_1 < num_3):
    print('Smallest is', num_1)
elif (num_2 < num_1) and (num_2 < num_3):
    print('Smallest is', num_2)
else:
    print('Smallest is', num_3)