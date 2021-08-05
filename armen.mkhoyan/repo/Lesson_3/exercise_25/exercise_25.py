#!/usr/bin/evn python3


four_digit_number = int(input("Enter four-digit number: "))

#option one
'''
if (four_digit_number >=1000) and (four_digit_number <10000):
    number_1 = four_digit_number//1000
    number_2 = (four_digit_number-(number_1*1000))//100
    number_3 = (four_digit_number - (number_1*1000)-(number_2*100))//10
    number_4 = four_digit_number - (number_1*1000)-(number_2*100)-(number_3*10)
    

    print(number_1,"+", number_2,"+", number_3,"+", number_4, "=", number_1+number_2+number_3+number_4)
else:
    print(" Please try again! Input four-digit number.")
'''
#option two
four_digit_number_string = str(four_digit_number)
if (four_digit_number >=1000) and (four_digit_number <10000):
    print("+".join(four_digit_number_string), "=",int(four_digit_number_string[0])+int(four_digit_number_string[1])+int(four_digit_number_string[2])+int(four_digit_number_string[3]))
else:
    print(" Please try again! Input four-digit number. ")