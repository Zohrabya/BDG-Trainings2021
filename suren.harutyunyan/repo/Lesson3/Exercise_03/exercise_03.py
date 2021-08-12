#! usr/bin/env python3


#a
print("a")

symbol="* "
print("",symbol,"\n", symbol, symbol,"\n", symbol,symbol,symbol,"\n", symbol,symbol,symbol,symbol)

#b

print("b")

# This is the example of print simple pyramid pattern  
n = 4  
# outer loop to handle number of rows  
for i in range(0, n):  
        for j in range(0, i + 1):  
            print("* ", end="")       
        print() 


#c
print("c")

symbol="* "
print(symbol)
print(symbol*2)
print(symbol*3)
print(symbol*4)


