#!/usr/bin/env python3 

lenght = float(input("Enter the lenght of the field (feets): "))
width = float(input("Enter the width of the field (feets): "))
#area in acre
ACRE = 43560 
print("Area is: ", round(lenght * width / ACRE, 2), "acres.")