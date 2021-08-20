#!usr/bin/evn python3

print ("Celsius", "\t", "Fahrenheit")
for i in range (0, 11):
    celsius = i * 10
    fahrenheit = (i * 10* 9 / 5) + 32
    print(celsius, "C", 2 * "\t", fahrenheit, "F")