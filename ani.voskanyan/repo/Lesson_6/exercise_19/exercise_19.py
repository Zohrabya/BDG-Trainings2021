#! /usr/bin/env python3

letters_list = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t" ,"u", "v", "w" , "x", "y", "z"]
text_input = input("Enter your text: ").lower().split()
transform = input("Encode or decode the text?").lower()

def caesar_encode_text(w):
    w = list(w)
    for i in range(0, len(w)):
        if w[i] in letters_list[0:23]:
            w[i] = letters_list[letters_list.index(w[i]) + 3]
        elif w[i] in letters_list[23:]:
           w[i] = letters_list[letters_list.index(w[i]) - 23]
        else:
            continue
    return w

def caesar_decode_text(w):
    w = list(w)
    for i in range(0, len(w)):
        if w[i] in letters_list[0:23]:
            w[i] = letters_list[letters_list.index(w[i]) - 3]
        elif w[i] in letters_list[23:]:
           w[i] = letters_list[letters_list.index(w[i]) + 23]
        else:
            continue
    return w

for word in text_input:
    word = list(word)
    if transform == "encode":
        result = "".join(caesar_encode_text(word))
    else:
        result = "".join(caesar_decode_text(word))
    print(result, end = " ")
