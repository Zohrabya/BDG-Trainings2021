#!/usr/bin/env python3

for i in range(1, 18):
    print(i, oct(i)[2:], (hex(i)[2:]).upper(), bin(i)[2:], sep = "\t")