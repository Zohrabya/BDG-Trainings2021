#!usr/bin/env python3

n_list = []
divisor_list = []
perfect_numbers = []

n = 1 
while n <= 100:
    n_list.append(n)
    n += 1
print(n_list)

for n in n_list:
    divisor = n 
    while divisor > 0:
        if n % divisor == 0:
            divisor_list.append(divisor)
        divisor -= 1
print(f'{n}  {divisor_list}')
