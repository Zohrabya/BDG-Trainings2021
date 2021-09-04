#!/usr/bin/env python3

with open("file_13.txt") as f:
    content = f.readlines()

with open("new_file", "w") as f:
    line_number = 1
    for line in content:
        f.write(f'{line_number}: {line}')
        line_number += 1
