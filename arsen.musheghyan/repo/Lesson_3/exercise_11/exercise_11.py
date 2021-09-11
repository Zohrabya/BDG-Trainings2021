import math
length = int(input("Please, enter length of a farmer’s field in feet: "))
width = int(input("Please, enter width of a farmer’s field in feet: "))
square = length * width 
print ("There are 43,560 square feet in an acre. ")
print ("The area of the field in acres is: ",math.ceil(square / 43560))