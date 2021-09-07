#!usr/bin/evn python3

list = []
sum = 0
for num in range(1, 101):
    for i in range (1, num + 1):
        if num % i == 0 and num not in list:
    #         list.append(num)
    # print (list)
            sum = i + sum
        if sum == num and num not in list:
            list.append(num)
print(list, "perfect numbers")