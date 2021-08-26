#!usr/bin/evn python3

list = []
word = str
while word != " ":
    word = input("Enter the words(enter a blank to exit): ")
    if word != " ":
        list.append(word)
        unique_words = sorted(set(list))
for item in(unique_words):
   print (item)

