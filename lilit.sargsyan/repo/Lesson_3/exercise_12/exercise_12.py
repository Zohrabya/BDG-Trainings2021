small_container = int(input("Enter the number of small containers you recycled: "))
large_container = int(input("Enter the number of large containers you recycled: "))
refund = (small_container * 0.10) + (large_container * 0.25)
print("The total refund for returning the containers is $" + "{0:.2f}".format(float(refund)))