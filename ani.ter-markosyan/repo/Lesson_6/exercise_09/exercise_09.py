#!usr/bin/evn python3

print ("Celsius", "\t", "Fahrenheit")
for i in range (0, 101):
    if i % 10 == 0:
        celsius = i
        fahrenheit = (i * 10 * 9 / 5) + 32
        print(celsius, "C", 2 * "\t", fahrenheit, "F")