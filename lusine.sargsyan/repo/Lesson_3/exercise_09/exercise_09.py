#! /usr/bin/env python3


a=input("enter the price of the meal:")
b=input("enter the desired tip in percents:")

a=int(a)
b=int(b)

c=a+a*b/100


print("tip:", b, "%", "\ntotal price:", c, "USD")