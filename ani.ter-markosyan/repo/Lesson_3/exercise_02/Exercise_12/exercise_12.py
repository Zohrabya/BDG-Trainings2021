size = float(input("Enter a size of container (liter): "))
number = float(input("Enter the number of containers: "))
if (size > 1):
    print("Your deposit is",round(number * 0.25,2),"$")
else:
    print("Your deposit is",round(number * 0.10,2), "$")    