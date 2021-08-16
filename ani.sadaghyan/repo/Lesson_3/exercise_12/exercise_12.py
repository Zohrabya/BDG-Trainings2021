#!usr/bin/evn python3
liter_or_less = int(input("Enter the number of containers"))
more_then_liter = int(input("Enter the number of  containers"))
print("the number for containers is", round(liter_or_less * 0.10, 2) + round(more_then_liter * 0.25, 2), "$")