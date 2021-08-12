# 16
first_num = int(input("Enter first number: "))
second_num = int(input("Enter second number: "))

if first_num > second_num:
    print(str(first_num) + " " + "is larger.")
elif second_num > first_num:
    print(str(second_num) + " " + "is larger.")
else:
    print("These numbers are equal.")