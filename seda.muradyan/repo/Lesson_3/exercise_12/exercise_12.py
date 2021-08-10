# Home work lesson 3/12
smallBottles = int(input("Enter bottles(1 liter or less) count: "))
bigBottles = int(input("Enter bottles(more than one liter) count: "))

smallBottlePrice = 0.10
bigBottlePrice = 0.25

outputSmallBottlesPrice = smallBottles * smallBottlePrice
outputBigBottlesPrice = bigBottles * bigBottlePrice

totalOutput = outputBigBottlesPrice + outputSmallBottlesPrice

output = "$" + "{:.2f}".format(totalOutput)
print(output)