#!/usr/bin/evn python3

entered_height = int(input("Enter the height of letter A: "))
i = 1
interval = 1
top = "*"
size = entered_height * 2
while i < entered_height:
    if i == 1:
        print(top.center(size))
    if i == int(entered_height/2):
        if entered_height % 2 == 0:
            line = (entered_height + 1) * "*"
        else:
            line = entered_height * "*"
        print(line.center(size))
        i += 1
        interval += 2
    row = "*" + interval * " " + "*"
    print(row.center(size))
    interval += 2
    i += 1
