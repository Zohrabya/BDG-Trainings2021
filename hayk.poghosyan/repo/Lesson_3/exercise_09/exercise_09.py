# 9
meal_price = int(input("Enter the price of the meal: "))
tip_percent = int(input("Enter the percent: "))
total_price = meal_price + (meal_price * tip_percent)/100
tip_percent_count = (meal_price * tip_percent)/100
print(tip_percent_count, "\n" ,total_price)