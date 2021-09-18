#!/usr/bin/env python3

print("Celsius\t", "Farenheit")
    
for celsius in range (0, 101, 10):
    farenheit = 9 / 5 * celsius + 32
    print(f'{celsius}\t{farenheit}')
    celsius += 10
