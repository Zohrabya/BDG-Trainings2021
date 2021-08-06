first = int(input("Insert first number \n"))
second = int(input("Insert second number \n"))
if first > second:
    print("{0} is larger {1}".format(first, second))
elif first < second:
    print("{0} is larger {1}".format(second, first))
else:
    print("This numbers are equal")
    