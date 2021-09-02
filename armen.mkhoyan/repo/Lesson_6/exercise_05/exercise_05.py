#!usr/bin/evn python3

"""
5.	Use for loops to print a diamond like the one below. 
Allow the user to specify how high the diamond should be.
"""

row = int(input("Enter a High: "))

for i in range(0, (row+1)//2, +1):

    print(" " * (row - i) + "*" * i + "*" * (i-1))

for i in range((row+1)//2, 0, -1):
    print(" " * (row - i) + "*" * i + "*" * (i-1))
