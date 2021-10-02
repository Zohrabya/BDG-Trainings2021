first = int(input("Insert first number \n"))
second = int(input("Insert second number \n"))
third = int(input("Insert third third \n"))

sum = first + second + third
product = first * second * third
print("avrage = {}".format(sum / 3))
print("product = {}".format(product))

if first > second > third:
    print("largest = {}".format(first))
elif second > first > third:
    print("largest = {}".format(second))
else:
    print("largest = {}".format(third))
    
if first < second < third:
    print("smallest = {}".format(first))
elif second < first < third:
    print("smallest = {}".format(second))
else:
    print("smallest = {}".format(third))



