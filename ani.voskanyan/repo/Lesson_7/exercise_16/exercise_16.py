#!/usr/bin/env python3

try:
    file_input = input("Enter the name of a file: ")
except FileNotFoundError:
    print("Nosuch file")

alphabet = list(map(chr, range(97, 123)))
my_dict = dict()

with open("file_input") as f:
    content = f.read().lower()
    content_list = list(content)

for letter in alphabet:
    if letter in content_list:
        my_dict[letter] = content.count(letter)

for key, value in my_dict.items():
    print(f'{key}: {value}')

print(f'The letter "{min(my_dict, key = my_dict.get).upper()}" is used in the smallest proportion of the words')
