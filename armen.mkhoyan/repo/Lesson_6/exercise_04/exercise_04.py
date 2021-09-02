#!usr/bin/evn python3

"""
4.	Use a for loop to print an upside down triangle like the one below. 
Allow the user to specify how high the triangle should be.
"""

high = int(input("Enter a High: "))


for i in range(high, 0, -1):
    print("*" * i)
