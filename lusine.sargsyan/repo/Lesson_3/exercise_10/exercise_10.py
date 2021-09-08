#!/usr/bin/env python3

unit = str(input("Enter the confortable for you mesuremnet unit (meter/feet): "))
width = float(input("Enter the width of the room: " ))
lenght = float(input("Enter the lenght of the room: "))
room_area = width * lenght
print("The room area is:", round(room_area, 2), unit) 