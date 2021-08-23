#! /usr/bin/env python3

text_input = input("Add a text to transform into Pig Latin: ").split(" ")
consonants = ["b", "c", "d", "f","g", "h", "j", "k", "l", "m", "n", "p","q", "r", "s","t", "v", "x", "w", "y", "z"]
upper_consonants, upper_vowels = [], []
vowels = ["a", "e", "i", "o", "u"]
punctuation_marks = [".", ",", "?", "!"]
result_list = []

for letter in consonants:
    upper_consonant = letter.upper()
    upper_consonants.append(upper_consonant)

for letter in vowels:
    upper_vowel = letter.upper()
    upper_vowels.append(upper_vowel)
    
print(text_input)

def transform_vowel(word):
    word.append("way")
    return word


def transform_consonant(word):
    done = True
    while done:
        if (word[0] in consonants) or (word[0] in upper_consonants):
            word.append(word[0])
            del word[0]
        else:
            done = False
    word.append("ay")

    return word


for word in text_input:
    word = list(word)
    last_char = ''
    
    if word[-1] in punctuation_marks:
        last_char = word.pop()

    if (word[0] in consonants) or (word[0] in upper_consonants):
        if word[0].isupper:
            result = "".join(transform_consonant(word)).lower().title()
        else:
            result = "".join(transform_consonant(word))
    else:
        result = "".join(transform_vowel(word))

    print(result + last_char)
