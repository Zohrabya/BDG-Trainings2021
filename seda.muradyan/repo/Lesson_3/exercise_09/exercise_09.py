# Home work lesson 3/9

price = float(input ("Enter price of the meal: "))
tipPracent = float(input ("Enter tip percent: "))

tipValue = price * tipPracent /100
totalValue = price + tipValue

print("total value is equal " + str(totalValue))
print("tip value is equal " + str(tipValue))