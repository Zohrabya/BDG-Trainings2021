#!usr/bin/evn python3

five_digit_number = int(input("Enter five-digit number: "))

#option one.
'''
if (five_digit_number >=10000) and (five_digit_number <100000):
    number_1 = five_digit_number//10000
    number_2 = (five_digit_number-(number_1*10000))//1000
    number_3 = (five_digit_number - (number_1*10000)-(number_2*1000))//100 
    number_4 = (five_digit_number - (number_1*10000)-(number_2*1000)-(number_3*100))//10
    number_5 = (five_digit_number - (number_1*10000)-(number_2*1000)-(number_3*100)-(number_4*10))
    

    print("Entered five-digit number separated: ", number_1, number_2, number_3, number_4, number_5)
else:
    print(" Please try again! Input five-digit number.")

'''
#option two
if (five_digit_number >=10000) and (five_digit_number <100000):
    five_digit_number_string = str(five_digit_number)
    print("  ".join(five_digit_number_string))
else:
    print(" Please try again! Input five-digit number.")