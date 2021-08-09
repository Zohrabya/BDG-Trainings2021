price = int(input('Enter the price of the meal:' ))
percent = int(input('Enter the percent of the tip:' ))
tip = price * percent / 100
bill_of_the_meal = price + tip
print('Tip amount is:', tip, '\nBill(the tip is included) is:', bill_of_the_meal, sep= ' ')