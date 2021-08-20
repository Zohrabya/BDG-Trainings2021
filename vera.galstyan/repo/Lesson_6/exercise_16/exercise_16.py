#!usr\bin\env python 3

word = input("Enter Pig Latin to translate: ")

#if the 1st letter of a word is "aeiou", add "way" to the end of the word 
if word[0] == "a" or "e" or "i" or "o" or "u":  
    print(word + "way")
elif word[0] and word[1] == "b" or "c" or "d" or "f" or "g" or "h" or "j" or "k" or "l" or "m" or "n" or "p" or "q" or "r" or "s" or "t" or "v" or "x" or "y" or "z":
    print(word + "ay")