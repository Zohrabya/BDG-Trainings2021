#!usr/bin/evn python 3

"""
6.	Write a program that prints a giant letter A like the one below. 
Allow the user to specify how large the letter should be.
"""

def letter_A(rows):
    for i in range(rows):
        for j in range(i,rows-1):
            print(' ',end='')
        for k in range(0,i+i+1):
          if k==0 or k==i+i or i==rows//2:
             print('*',end='')
          else: print(' ',end='')
        
        print()


letter_A(int(input("Enter a Letter Size: ")))

