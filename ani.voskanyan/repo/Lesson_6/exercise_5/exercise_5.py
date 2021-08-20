#!usr/bin/env python3

height = int(input("Enter the height of the diamond: "))

for i in range(0, int(height/2)):
        print(("*" + i * "*" * 2).center(height, " "))

if height % 2 != 0:
    for y in range(int(height/2), 0, -1): 
        print(("*" + y * "*" * 2).center(height, " "))
else:
    for y in range(int(height/2) - 1, 0, -1): 
        print(("*" + y * "*" * 2).center(height, " "))
            
print("*".center(height, " "))
