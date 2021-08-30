first = int(input("Insert first number: "))
second = int(input("Insert second number: "))
if first % second == 0:
    print(first, "is a multiple of the", second)
else:
    print(first, "is not a multiple of the", second)
