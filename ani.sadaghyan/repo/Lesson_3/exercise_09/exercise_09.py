meal = float(input("Write price of the meal: "))
percent  = int(input("Percent tip: "))
tip = meal * percent / 100
print ("Your price for tip: ", tip)
print ("Total amount: ", meal + tip)