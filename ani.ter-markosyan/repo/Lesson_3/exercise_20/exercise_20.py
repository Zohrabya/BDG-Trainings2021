#!usr/bin/evn python3
# num1, num2, num3, num4, num5 = map(int,input("Enter five different numbers: ").split())
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
num3 = int(input("Enter third number: "))
num4 = int(input("Enter fourth number: "))
num5 = int(input("Enter fifth number: "))
largest = max(num1, num2, num3, num4, num5)
smallest = min(num1, num2, num3, num4, num5)
print("Largest is", largest, "\n", "Smallest is", smallest)