length = int(input("Enter the length (in feet): "))
width = int(input("Enter the width (in feet): "))
ACRE = 43560
print("The area of a field is", round(width * length / ACRE, 2), "acres.")
