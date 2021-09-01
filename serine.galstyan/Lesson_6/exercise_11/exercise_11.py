#!/usr/bin/evn python3

collection_of_words = []
entered_word = input("Enter word: (blank to quit): ")
while entered_word != "":
    if entered_word not in collection_of_words:
        collection_of_words += [entered_word]
        continue
    entered_word = input("Enter word: (blank to quit): ")
    if entered_word == "":
        print(collection_of_words)
