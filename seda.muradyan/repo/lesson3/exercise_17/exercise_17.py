num_1, num_2, num_3 = input("enter three numbers: ").split()

print("Sum is: ", int(num_1 + num_2 + num_3))
print("Average is: ", round(float(num_1) + int(num_2 + num_3)) / 3)
print("Product is: ", int(num_1) *int(num_2) * int(num_3))

if num_1 < num_2:
    if  num_1 < num_3: 
     print("Smallest is: ", num_1)
elif num_2 < num_3: 
    print("Smallest is: ", num_2)
else: 
    print("Smallest is: ", num_3)  

if num_1 > num_2: 
    if num_1 > num_3: 
     print("Largest is: ", num_1)
elif num_2 > num_3:
    print("Largest is: ", num_2)
else: 
    print("Largest is: ", num_3)