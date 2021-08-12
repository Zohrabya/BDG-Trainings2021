# 17
num_1 = int(input("Enter num1: "))
num_2 = int(input("Enter num2: "))
num_3 = int(input("Enter num3: "))
sum = num_1 + num_2 + num_3
average = sum / 3
product = num_1 * num_2 * num_3 
print("Input three different integers: " " " + str(num_1) + " " + str(num_2) + " " + str(num_3))
print("Sum is: " + str(sum))
print("Average is: " + str(average))
print("Product is: " + str(product))
if num_1 < num_2 and num_1 < num_3:
    print("Smallest is: " + str(num_1))
elif num_2 < num_1 and num_2 < num_3:
    print("Smallest is: " + str(num_2))
else:
    print("Smallest is: " + str(num_3))

if num_1 > num_2 and num_1 > num_3:
    print("Largest is: " + str(num_1))
elif num_2 > num_1 and num_2 > num_3:
    print("Largest is: " + str(num_2))
else:
    print("Largest is: " + str(num_3))