#!/usr/bin/env python3

length_room = float(input("Enter the length of the room: "))
width_room = float(input("Enter the width of the room: "))
unit_of_measurement = input("Select the unit you are more comfortable working with (meters or feet):  ")
area_room = length_room * width_room
print("The area is", round(area_room, 2), unit_of_measurement)
