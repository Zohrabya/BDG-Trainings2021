#!usr/bin/evn python3

# num1, num2, num3, num4, num5 = map(int,input("Enter five different numbers: ").split())
#largest = max(num1, num2, num3, num4, num5)
#smallest = min(num1, num2, num3, num4, num5)

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
num3 = int(input("Enter third number: "))
num4 = int(input("Enter fourth number: "))
num5 = int(input("Enter fifth number: "))
if num1 > num2 and num1 > num3 and num1 >num4 and num1 > num5:
    print("Largest is", num1)
elif num2 > num1 and num2 > num3 and num2 > num4 and num2 > num5:
    print("Largest is", num2)
elif num3 > num1 and num3> num2 and num3> num4 and num3 > num5:
    print("Largest is", num3)
elif num4 > num1 and num4 > num2 and num4 > num3 and num4 > num5:
    print("Largest is", num4)
elif num5 > num1 and num5 > num2 and num5 > num3 and num5 > num4:
    print("Largest is", num5)
if num1 < num2 and num1 < num3 and num1 < num4 and num1 < num5:
    print("Smallest is", num1)
elif num2 < num1 and num2 < num3 and num2 < num4 and num2 < num5:   
    print("Smallest is", num2)
elif num3 < num1 and num3 < num2 and num3 < num4 and num3 < num5:
    print("Smallest is", num3)
elif num4 < num1 and num4 < num2 and num4 < num3 and num4 < num5:
    print("Smallest is", num4)
elif num5 < num1 and num5 < num2 and num5 < num3 and num5 < num4:
    print("Smallest is", num5)