inp_number1 = int(input("Enter a number: "))
inp_number2 =  int(input("Enter a number: "))
inp_number3 =  int(input("Enter a number: "))
inp_number4 =  int(input("Enter a number: "))
inp_number5 =  int(input("Enter a number: "))


if inp_number3 < inp_number1 > inp_number2 and inp_number4 < inp_number1 > inp_number5:
    largest_number = inp_number1
elif inp_number1 < inp_number2> inp_number3 and inp_number4 < inp_number2 > inp_number5:
    largest_number= inp_number2
elif inp_number1 < inp_number3 > inp_number2 and inp_number4 < inp_number3 > inp_number5:
    largest_number = inp_number3
elif inp_number1 < inp_number4 > inp_number2 and inp_number3 < inp_number4 > inp_number5:
    largest_number= inp_number4
elif inp_number1 < inp_number5 > inp_number2 and inp_number3 < inp_number5 > inp_number4:
    largest_number= inp_number5
print("The largest number is {}:".format(largest_number))


if inp_number3 > inp_number1 < inp_number2 and inp_number4 > inp_number1 < inp_number5:
    smallest_number = inp_number1
elif inp_number1 > inp_number2 < inp_number3 and inp_number4 > inp_number2 < inp_number5:
    smallest_number = inp_number2
elif inp_number1 > inp_number3 < inp_number2 and inp_number4 > inp_number3 < inp_number5:
    smallest_number = inp_number3
elif inp_number1 > inp_number4 < inp_number2 and inp_number3 > inp_number4 < inp_number5:
    smallest_number = inp_number4
elif inp_number1 > inp_number5 < inp_number2 and inp_number3 >  inp_number5 < inp_number4:
    smallest_number = inp_number5
print("The smallest number is {}:".format(smallest_number))