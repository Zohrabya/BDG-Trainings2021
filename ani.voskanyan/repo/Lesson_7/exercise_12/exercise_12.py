 #!/usr/bin/env python3

try:
    numerator = int(input("Enter numerator of a fraction: "))
except ValueError:
    print("Wrong input. Enter only integers.")
    numerator = int(input("Enter numerator of a fraction: "))

try:
    denominator = int(input("Enter denominator of a fraction: "))
except ValueError:
    print("Wrong input. Enter only integers")
    denominator = int(input("Enter denominator of a fraction: "))

if denominator == 0:
    raise ZeroDivisionError("You can't divide on Null.")


def reduce_fraction(n, d):
    min_fraction = n if n <= d else d

    for s in range(min_fraction + 1, 1, -1):
        print(s)

        if n % s == 0 and d % s == 0:
            n /= s
            d /= s
            break
    return f'{int(n)}/{int(d)}'


print(reduce_fraction(numerator, denominator))
