integer_1 = int(input("Enter the first integer:"))
integer_2 = int(input("Enter the second integer: "))
integer_3 = int(input("Enter the third integer"))

integers_sum = integer_1 + integer_2 + integer_3
integers_average = int(integers_sum / 3)
integers_product = integer_1 * integer_2 * integer_3

if integer_1 < integer_2 and integer_1 < integer_3:
    smallest_integer = integer_1
elif integer_2 < integer_1 and integer_2 < integer_3:
    smallest_integer = integer_2
else:
    smallest_integer = integer_3

if integer_1 > integer_2 and integer_1 > integer_3:
    largest_integer = integer_1
elif integer_2 > integer_1 and integer_2 > integer_3:
    largest_integer = integer_2
else:
    largest_integer = integer_3

print(f"""Input three different integers: {integer_1} {integer_2} {integer_3}
Sum is {integers_sum}
Average is {integers_average}
Product is {integers_product}
Smallest is {smallest_integer}
Largest is {largest_integer}""")
