#!usr/bin/evn python3


def ordinal(num):
    for i in range(1,13):
        if i == 1:
            print(num = i + "st")
        elif i == 2:
            print(num = i +"nd")
        elif i == 3:
            print(num = i + "rd")
        else:
            print(num = i +"th")
        if i > 13 or i < 1:
            raise ValueError(" ")
    print(ordinal(num))
        