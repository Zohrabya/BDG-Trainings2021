#!/usr/bin/env python3

text_input = input("Add a text to transform into Pig Latin: ").lower().split(" ")
consonants = ["b", "c", "d", "f","g", "h", "j", "k", "l", "m", "n", "p","q", "r", "s","t", "v", "x", "w", "y", "z"]
vowels = ["a", "e", "i", "o", "u"]

print(text_input)


def transform_vowel(word):
  word.append('way')
  return word


def transform_consonant(word):
  done = True
  
  while done:
    if word[0] in consonants:
        word.append(word[0])
        del word[0]
    else: 
        done = False
  
  word.append('ay')
  return word

for word in text_input:
    word = list(word)

    if word[0] in consonants:
        result = transform_consonant(word)
    else:
        result = transform_vowel(word)
    
    print("".join(result), end=" ")
