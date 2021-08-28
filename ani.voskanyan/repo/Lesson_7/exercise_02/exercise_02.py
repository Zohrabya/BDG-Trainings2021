#!usr/bin/env python3

args_list = []

def arguments_input():
    while len(args_list) < 3:
        arg_input = float(input(f"Please enter a value N{len(args_list) + 1}: "))
        args_list.append(arg_input)
        

def calculate_median(*list):
    sorted_list = sorted(list)
    print(sorted_list[1])


try:
   arguments_input()
except ValueError: 
    print("You can enter only numbers!")
    arguments_input()

calculate_median(*args_list) 
