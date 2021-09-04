inp_number1 = int(input("Enter a number: "))
inp_number2 =  int(input("Enter a number: "))
inp_number3 =  int(input("Enter a number: "))

sum_numbers = inp_number1 + inp_number2 + inp_number3

averege_numbers = sum_numbers / 3

product_numbers = inp_number1 * inp_number2 * inp_number3
#largest_number
if inp_number2 < inp_number1 > inp_number3:
    largest_number = inp_number1    
elif inp_number1 < inp_number2 > inp_number3:
    largest_number = inp_number2
elif inp_number1 < inp_number3 > inp_number2:
    largest_number = inp_number3

#smallest_number
if inp_number2 > inp_number1 < inp_number3:
    smallest_number = inp_number1    
elif inp_number1 > inp_number2 < inp_number3:
    smallest_number = inp_number2
elif inp_number1 > inp_number3 < inp_number2:
    smallest_number = inp_number3


print(f"Input three deferent integers: {inp_number1} {inp_number2} {inp_number3} \nSum is {sum_numbers} \nAverage is {averege_numbers} \nProduct is {product_numbers} \nSmallest is {smallest_number} \nLargest is {largest_number}")

