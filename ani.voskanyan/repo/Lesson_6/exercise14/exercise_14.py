#!usr/bin/env python3

n_list = []
divisor_list = []
perfect_numbers = []

n = 1 
while n <= 100:
    n_list.append(n)
    n += 1

for n in n_list:
    divisor = n - 1
    while divisor > 0:
        if n % divisor == 0:
            divisor_list.append(divisor)
        divisor -= 1
    if sum(divisor_list) == n:
        perfect_numbers.append(n)
    divisor_list.clear()

print(perfect_numbers)
