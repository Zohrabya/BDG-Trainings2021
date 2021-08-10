# Home work lesson 3/13

price = float(input ("Enter price of the meal: "))

taxPracent = 22
tipPracent = 18

tipValue = price * tipPracent /100
taxValue = price * taxPracent /100
totalValue = price + tipValue + taxValue

print("total value is equal: " + "{:.2f}".format(totalValue))
print("tip value is equal: " + "{:.2f}".format(tipValue))
print("tax value is equal: " + "{:.2f}".format(taxValue))
