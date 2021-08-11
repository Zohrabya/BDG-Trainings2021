cost = int(input("Enter the cost of your meal: "))
TAX_RATE = 5.2
tax = (round(TAX_RATE * cost  / 100,2))
tip = (round(18 * cost / 100,2))
total = (round(tax + tip + cost, 2))
# print("Tax amount is: ", tax, "tip amount is: ", tip, "grand total is: ", total)
#I think the following variant is more beautiful and readable 
print("Tax amount is: ", tax, end = "\n"), print("Tip amount is: ", tip, end = "\n"), print("Grand total is: ", total)

