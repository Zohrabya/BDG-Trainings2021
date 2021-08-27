#!/usr/bin/env python3
print("Celsius", "\t", "Farenheit")
for item in range(1, 11):
    celsius = item * 10
    farenheit = (9/5 * celsius) + 32
    print(celsius, "°C", 2 * "\t", farenheit, "°F")


