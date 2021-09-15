def validTriangle(side1, side2, side3):
    if side1 >= (side2 + side3) or side2 >= (side1 + side3) or side3 >= (side2 + side1):
        return False
    else:
        return True

if __name__ == '__main__':
    side1 = int(input('Enter side 1: '))
    side2 = int(input('Enter side 2: '))
    side3 = int(input('Enter side 3: '))
    if validTriangle(side1, side2, side3):
        print('Three lengths can form a triangle')
    else:
        print('Three lengths cannot form a triangle')