num_1= int(input('Enter the first integer: '))
num_2= int(input('Enter the second integer: '))
num_3= int(input('Enter the third integer: '))
num_4= int(input('Enter the fourt integer: '))
num_5= int(input('Enter the fifth integer: '))
if (num_1 < num_2) and (num_1 < num_3) and (num_1 < num_4) and (num_1 < num_5):
    print('Smallest is', num_1)
elif  (num_2 < num_1) and (num_2 < num_3) and (num_2 < num_4) and (num_2 < num_5):
    print('Smallest is', num_2)
elif  (num_3 < num_1) and (num_3 < num_2) and (num_3 < num_4) and (num_3 < num_5):
    print('Smallest is', num_3)
elif  (num_4 < num_1) and (num_4 < num_2) and (num_4 < num_3) and (num_4 < num_5):
     print('Smallest is', num_4)
else:
    print('Smallest is', num_5)
if (num_1 > num_2) and (num_1 > num_3) and (num_1 > num_4) and (num_1 > num_5):
    print('Largest is', num_1)
elif  (num_2 > num_1) and (num_2 > num_3) and (num_2 > num_4) and (num_2 > num_5):
    print('Largest is', num_2)
elif  (num_3 > num_1) and (num_3 > num_2) and (num_3 > num_4) and (num_3 > num_5):
    print('Largest is', num_3)
elif  (num_4 > num_1) and (num_4 > num_2) and (num_4 > num_3) and (num_4 > num_5):
     print('Largest is', num_4)
else:
    print('Largest is', num_5)