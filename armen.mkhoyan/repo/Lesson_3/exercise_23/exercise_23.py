#!usr/bin/evn python3

five_digit_number = int(input("Enter five-digit number: "))

if 10000 <= five_digit_number < 100000:
    five_digit_number_string = str(five_digit_number)
    print("  ".join(five_digit_number_string))
else:
    print(" Please try again! Input five-digit number.")