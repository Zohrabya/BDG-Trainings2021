#!usr\bin\env python 3\

try:
    number_input = int(input("Enter a number: "))
except ValueError:
    print("You can input only integers. Try again")
    number_input = int(input("Enter a number: "))


def prime_number(num):
    i = num - 1
    while i > 1:
        if num % i == 0:
            return False
        else:
            i -= 1
            continue
    return True
    

def next_prime(n):
    n += 1
    while prime_number(n) is False:
        n += 1
    else:
        return n


print(next_prime(number_input))
