#! usr/bin/env python3

#a

print("a")

header_and_footer="\n*****************"
fill="\n*               *"
print(header_and_footer,fill,fill,header_and_footer)

#b

print("b")


w=17
empty_space=" "
n=13
symbol="*"

print(symbol*w)
print(symbol,empty_space*n,symbol)
print(symbol,empty_space*n,symbol)
print(symbol*w)

#c

print("c")

w=17

product=('*')

print(product * w)

for i in range(w-15):

    print(product,(w-4) * (' '),product)

print(product * w)

