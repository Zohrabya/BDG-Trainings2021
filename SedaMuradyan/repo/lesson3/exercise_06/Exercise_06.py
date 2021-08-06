num = int(input("Enter a number" + "\n"))

output = num

max = 6

for i in range(2, max):

    output = str(output) + "---" + str(num * i)

print(output)