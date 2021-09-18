#!/usr/bin/env python3

import random

lottery_numbers = []

while len(set(lottery_numbers)) < 6:
    n = random.randrange(1, 50)
    lottery_numbers.append(n)
    
print("Lottery numbers")
for y in sorted(list(set(lottery_numbers))):
    print(y, end = " ")
print()
