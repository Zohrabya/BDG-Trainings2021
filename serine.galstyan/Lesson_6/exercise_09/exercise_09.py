#!/usr/bin/evn python3

degree_in_Celsius = 0
print("Degrees in Celsius\t\t\tDegrees in Fahrenheit")
while degree_in_Celsius <= 100:
    degree_in_Fahrenheit = degree_in_Celsius * 1.8 + 32
    print(degree_in_Celsius, round(degree_in_Fahrenheit, 2), sep="\t\t\t\t\t")
    degree_in_Celsius += 1
