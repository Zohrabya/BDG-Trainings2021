#!usr/bin/env python3
words = []
new_word = input("Enter a word: ")

while new_word != '':
    words.append(new_word)
    new_word = input("Enter another word: ")
else:
    words_output = set(words)
    print(words_output)
