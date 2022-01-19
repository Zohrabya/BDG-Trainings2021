#!usr/bin/evn python3

short_side1 = int(input("Enter the lenght of triangle's 1 side: "))
short_side2 = int(input("Enter the lenght of trangle's 2 sede: "))
def triangle_hyp(short_side1, short_side2):
    if short_side1 == 0 or short_side2 == 0:
        raise ValueError("The lenght of triangle's side can not be zero.")
    else:
         return (short_side1 ** 2 + short_side2 ** 2) ** 0.5
print(f"Triangle's hypotenus is {triangle_hyp(short_side1, short_side2)}.")

