#!usr\bin\env python 3

n = int(input("Enter a positive integer: "))
divisors_list = []

divisor = int(n / 2)
while divisor > 0:
    if n % divisor == 0:
        divisors_list.append(divisor)
    divisor -= 1

print(divisors_list)
