#!usr/bin/env python3

words_entered = list()
user_word = input("Please enter the word: ")
while user_word != "":
    if user_word not in words_entered:
        words_entered.append(user_word)
    user_word = input("Please enter the word: ")
for item in words_entered:
    print(item)