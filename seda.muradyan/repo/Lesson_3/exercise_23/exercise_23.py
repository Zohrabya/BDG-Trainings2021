print("Enter a 5 digit whole number: ")
num = int(input())
digit5 = num % 10
num = int(num / 10)
digit4 = num % 10
num = int(num / 10)
digit3 = num % 10
num = int(num / 10)
digit2 = num % 10
num = int(num / 10)
digit1 = num % 10
print(digit1,"   ",digit2,"   ",digit3,"   ",digit4,"   ",digit5,"\n")

