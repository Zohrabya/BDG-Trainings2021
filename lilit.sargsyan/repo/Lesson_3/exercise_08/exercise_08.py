first_num = int(input('Enter first number: ' ))
second_num = int(input('Enter second number: ' ))
third_num = int(input('Enter third number: '))
total = first_num + second_num + third_num
average = total / 3
average_format = '{:.2f}' .format(average)
print('Total:', total, '\nAverage:', (average_format))