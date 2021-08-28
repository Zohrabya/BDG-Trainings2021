#!usr/bin/env python3

try:
    string_input = input("Please enter your text: ")
    width = int(input("Please enter the width of the terminal: "))
except ValueError:
        print("The width of the terminal can be only an integer. Try again.")
        width = int(input("Please enter the width of the terminal: "))


def str_center(s, w):
    spaces_num = int((w - len(s)) / 2) + len(s)
    print(s.rjust(spaces_num, " "))

str_center(string_input, width)
