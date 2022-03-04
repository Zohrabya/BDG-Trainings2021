#!/usr/bin/env python3

user_input = input("Please type a text: ")
dirrection = input("Encode or decode the text? ")
result = ""

for i in range(len(user_input)):
    if dirrection == "decode":
        result = result + chr(ord(user_input[i]) + 3)
    else:
        result = result +chr(ord(user_input[i]) - 3)
print(result)