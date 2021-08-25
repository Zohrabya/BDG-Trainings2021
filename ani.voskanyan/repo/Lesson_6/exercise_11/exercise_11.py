#!usr/bin/env python3

words, words_output = [], []
new_word = input("Enter a word: ")

while new_word != '':
    words.append(new_word)
    new_word = input("Enter another word: ")
else:
    for w in words:
        if w in words_output:
            continue
        else:
            words_output.append(w)
    print(words_output)
