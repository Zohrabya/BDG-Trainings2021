#!usr/bin/evn python3

list1 = []
for i in range (3):
    element = input("enter the element: ")
    assert element != "0", "Entered number should not be zero."
    list1.append(element)
    list1.sort()
def average(list1):
    index = len(list1) // 2
    return(list1[index])
print (average(list1))

