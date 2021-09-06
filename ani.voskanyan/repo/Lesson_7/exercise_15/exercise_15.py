#!/usr/bin/env python3

file_input = input("Enter the name of a file: ")
output_file = input("Enter the name of a new file: ")

with open(file_input) as f:
    content = f.readlines() 

with open(output_file, "w") as f:
    for line in content:
        line_list = list(line)
        if "#" in line_list:
            del  line_list[line.find("#") :]
        f.write("".join(line_list))
        f.write("\n")
