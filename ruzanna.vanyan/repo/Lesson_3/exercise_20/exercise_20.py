num1 = int(input("Enter a number"))
num2 =  int(input("Enter a number"))
num3 =  int(input("Enter a number"))
num4 =  int(input("Enter a number"))
num5 =  int(input("Enter a number"))
#largest
if num3 < num1 > num2 and num4 < num1 > num5:
    largest = num1
elif num1 < num2 > num3 and num4 < num2 > num5:
    largest = num2
elif num1 < num3 > num2 and num4 < num3 > num5:
    largest = num3
elif num1 < num4 > num2 and num3 < num4 > num5:
    largest = num4
elif num1 < num5 > num2 and num3 < num5 > num4:
    largest = num5
print("Tha largest number is {}:".format(largest))

#smallest
if num2 > num1 < num3 and num4 > num1 < num5:
    smallest = num1
elif num1 > num2 < num3 and num4 > num2 < num5:
    smallest = num2
elif num1 > num3 < num2 and num4 > num3 < num5:
    smallest = num3
elif num1 > num4 < num2 and num3 > num4 < num5:
    smallest = num4
elif num1 > num5 < num2 and num3 > num5 < num4:
    smallest = num5
print("The smallest number is {}:".format(smallest))
