num_1 = int(input('Enter the first integer: '))
num_2 = int(input('Enter the second integer: '))
num_3 = int(input('Enter the third integer: '))
num_4 = int(input('Enter the fourt integer: '))
num_5 = int(input('Enter the fifth integer: '))

if (num_2 or num_3) and  (num_4 or num_5) > num_1 :
    print('Smallest is', num_1)
elif (num_1 or num_3) and (num_4 or num_5) > num_2 :
    print('Smallest is', num_2)
elif (num_1 or num_2) and (num_4 or num_5) > num_3 :
    print('Smallest is', num_3)
elif (num_1 or num_2) and (num_3 or num_5) > num_4 :
     print('Smallest is', num_4)
else:
    print('Smallest is', num_5)

if (num_2 or num_3) and (num_4 or num_5) < num_1 :
    print('Largest is', num_1)
elif (num_1 or num_3) and (num_4 or num_5) < num_2 :
    print('Largest is', num_2)
elif (num_1 or num_2) and (num_4 or num_5) < num_3 :
    print('Largest is', num_3)
elif (num_1 or num_2) and (num_3 or num_5) < num_4 :
     print('Largest is', num_4)
else:
    print('Largest is', num_5)