#!usr\bin\env python 3\

try:
    number_input = int(input("Enter a number: "))
except ValueError:
    print("You can input only integers. Try again")
    number_input = int(input("Enter a number: "))


def prime_number(n):
    i = n - 1
    while i > 1:
        if n % i == 0:
            return False
        else:
            i -= 1
            continue

    return True


print(prime_number(number_input))
