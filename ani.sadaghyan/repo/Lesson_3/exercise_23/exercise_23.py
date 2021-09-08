num = input("Enter a five-digit number: ")
if len(num) == 5:
    print(num[0], num[1], num[2], num[3], num[4], sep = " "*3)
else:
    print("Enter a five-digit num!")