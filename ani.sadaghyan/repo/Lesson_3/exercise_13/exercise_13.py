cost = int(input("Enter the cost of your meal: "))
RATE_TIP = 18
RATE_TAX = 5.2
tip = RATE_TIP * cost  / 100
tax = RATE_TAX * cost / 100
total = tax + tip + cost
print("Tax amount is: ", round(tax, 2), "\nTip amount is: ", round(tip, 2), "\nGrand total is: ", round(total, 2))