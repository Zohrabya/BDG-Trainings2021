#!usr/bin/evn python3

cost = int(input("Enter the cost of your meal: "))
TAX_RATE = 5.2
TIP_RATE = 18
tax = (round(TAX_RATE * cost  / 100, 2))
tip = (round( TIP_RATE * cost / 100, 2))
total = (round(tax + tip + cost, 2))
print("Tax amount is: ", tax, "\nTip amount is: ", tip, "\nGrand total is: ", total)