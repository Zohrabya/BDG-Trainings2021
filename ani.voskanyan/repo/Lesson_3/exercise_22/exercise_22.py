integer_1 = int(input("Please enter the first integer:"))
integer_2 = int(input("Please enter the second integer: "))

if integer_1 % integer_2 == 0:
    print(f' {integer_1} is a multiple of {integer_2}')
else:
    print(f" {integer_1} isn't a multiple of {integer_2}")
    