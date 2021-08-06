meal_price = float(input("Please, tell price of the meal: "))
percent_tip = int(input("Percent tip: "))
tip_amount = meal_price * percent_tip / 100
total = meal_price + tip_amount
print(f"Tip amount is {tip_amount}. Your total bill is equal to {total}")
