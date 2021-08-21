#! /usr/bin/env python3

import random

lottery_numbers = []
guessed_numbers = []

i = 1
while i <= 6: 
    my_num = int(input(f'"Guess number N {i}: '))
    guessed_numbers.append(my_num)
    i += 1

print("Guessed numbers")
for k in guessed_numbers:
    print(k, end = " ")
print()

while len(set(lottery_numbers)) < 6:
    n = random.randrange(1, 50)
    lottery_numbers.append(n)
    
print("Lottery numbers")
for y in set(lottery_numbers):
    print(y, end = " ")
print()

result = (set(lottery_numbers)).intersection(guessed_numbers)

if len(result) != 6:
    print("You failed")
else:
    print("Congratulations. You won")
