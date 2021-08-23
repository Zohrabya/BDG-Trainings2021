#!usr\bin\env python 3

triangle_sides = []
fill = True 

while fill:
    try:
        if len(triangle_sides) < 2:
            side = float(input("Enter the first side of a right triangle: "))
            triangle_sides.append(side)
        if len(triangle_sides) == 2:
            fill = False
    except ValueError:
        print("You can enter only numbers. Please try again")
            
            
def calculate_hypotenuse(a, b):    
    c = (a ** 2 + b ** 2) ** (1 / 2)
    return c


print(f'The hypotenuse of the triangle is {calculate_hypotenuse(triangle_sides[0], triangle_sides[1]):.2f}')
