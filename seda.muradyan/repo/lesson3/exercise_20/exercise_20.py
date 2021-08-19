number_1 = int(input("Enter a first number: "))
number_2 = int(input("Enter a second number: "))
number_3 = int(input("Enter a third number: "))
number_4 = int(input("Enter a fourth number: "))
number_5 = int(input("Enter a fifth number: "))

print("Entered five different numbers: ", number_1, number_2, number_3, number_4,number_5)

#smallest
if number_1<=number_2 and number_1<=number_3 and number_1<=number_4 and number_1<=number_5:
    print("Smallest is ", number_1)
elif number_2<=number_1 and number_2<=number_3 and number_2<=number_4 and number_2<=number_5:
    print("Smallest is ", number_2)
elif number_3<=number_1 and number_3<=number_2 and number_3<=number_4 and number_3<=number_5:
    print("Smallest is ", number_3)
elif number_4<=number_1 and number_4<=number_2 and number_4<=number_3 and number_4<=number_5:
    print("Smallest is ", number_4)
elif number_5<=number_1 and number_5<=number_2 and number_5<=number_3 and number_5<=number_4:
    print("Smallest is ", number_5)

#largest
if number_1>=number_2 and number_1>=number_3 and number_1>=number_4 and number_1>=number_5:
    print("Largest is ", number_1)
elif number_2>=number_1 and number_2>=number_3 and number_2>=number_4 and number_2>=number_5:
    print("Largest is ", number_2)
elif number_3>=number_1 and number_3>=number_2 and number_3>=number_4 and number_3>=number_5:
    print("Largest is ", number_3)
elif number_4>=number_1 and number_4>=number_2 and number_4>=number_3 and number_4>=number_5:
    print("Largest is ", number_4)
elif number_5>=number_1 and number_5>=number_2 and number_5>=number_3 and number_5>=number_4:
    print("Largest is ", number_5) 