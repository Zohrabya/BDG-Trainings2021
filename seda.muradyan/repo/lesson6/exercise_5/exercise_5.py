h = eval(input("please enter diamond's height:"))

for x in range(h):
    print(" "*(h-x), "*"*(x*2+1))
for x in range(h-2, -1, -1):
    print(" "*(h-x), "*"*(x*2+1))