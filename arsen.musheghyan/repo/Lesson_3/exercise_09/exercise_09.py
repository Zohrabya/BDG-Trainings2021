meal = int(input("Write price of the meal: "))
percent  = int(input("How many percent tip do you want to leave: "))
tip = meal * percent / 100
print ("Your price for tip: ", tip)
print ("Total amount: ", meal + tip)