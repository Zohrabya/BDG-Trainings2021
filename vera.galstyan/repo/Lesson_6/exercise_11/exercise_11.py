#!usr\bin\env python3

firstName = input("What \nis \nyour \nfirst \nname?:")
def find_vowels(firsName):
   
   for letter in firstName:
    if letter == "-":
        print("There is an a in your name, first fount at index") + str(firstName.find(letter))
    break