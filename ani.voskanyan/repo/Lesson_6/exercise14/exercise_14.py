#!usr/bin/env python3

divisor_list = []
perfect_numbers = []

for n in range (1, 101):
    divisor = n - 1
    while divisor > 0:
        if n % divisor == 0:
            divisor_list.append(divisor)
        divisor -= 1
    if sum(divisor_list) == n:
        perfect_numbers.append(n)
    divisor_list.clear()

print(perfect_numbers)
