#!usr\bin\env python 3

side_1 = float(input("Enter the first side of a right triangle: "))
side_2 = float(input("Enter the second side of a right triangle: "))

def calculate_hypotenuse(a, b):
    c = (a ** 2 + b ** 2) ** (1 / 2)
    return c

print(f'The hypotenuse of the triangle is {calculate_hypotenuse(side_1, side_2):.2f}')
