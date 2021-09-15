#!/usr/bin/env python3

text_input = input("Add a text to transform into Pig Latin: ").lower().split(" ")
consonants = ["b", "c", "d", "f","g", "h", "j", "k", "l", "m", "n", "p","q", "r", "s","t", "v", "x", "w", "y", "z"]
vowels = ["a", "e", "i", "o", "u"]

print('The origin text is "' + ' '.join(text_input) + '"')


def transform_vowel(word):
    return word + 'way'


def transform_consonant(word):
    i = 0
    while word[i] in consonants:
        i += 1
  
    word = word[i :] + word[0 : i]   
    return word + 'ay'

for word in text_input:
    if word[0] in consonants:
        result = transform_consonant(word)
    else:
        result = transform_vowel(word)
    
    print("".join(result), end=" ")
