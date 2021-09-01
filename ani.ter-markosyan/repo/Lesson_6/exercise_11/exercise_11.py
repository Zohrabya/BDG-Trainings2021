#!usr/bin/evn python3

list = []
word = str
while word != "":
    word = input("Enter the words(enter a blank to exit): ")
    if word not in list and word!="":
        list.append(word)
for item in list:
    print(item)
