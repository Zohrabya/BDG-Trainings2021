#!/usr/bin/evn python3


four_digit_number = int(input("Enter four-digit number: "))

if 1000 <= four_digit_number <10000:
    print("+".join(str(four_digit_number)), "=",int(str(four_digit_number)[0])+int(str(four_digit_number)[1])+int(str(four_digit_number)[2])+int(str(four_digit_number)[3]))
else:
    print(" Please try again! Input four-digit number. ")