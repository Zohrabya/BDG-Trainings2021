#!/usr/bin/env python3 

lenght = float(input("Enter the lenght of the field (feets): "))
width = float(input("Enter the width of the field (feets): "))
#area in acre
acre = 43560 
print("area is: ", round(lenght * width / acre, 2), "acres.")