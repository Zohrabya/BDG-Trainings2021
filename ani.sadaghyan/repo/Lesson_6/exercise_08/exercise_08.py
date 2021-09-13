#!/usr/bin/env python3

numbers = [4.95, 9.95, 14.95, 19.95, 24.95]
i = 0
tokos = 0
for i in range(0,len(numbers),2): 
    tokos = (numbers[i] -(numbers[i] * 0.6))
    print(tokos,  numbers[i])
