# 9
price = int(input("Enter the price of the meal:"))
percent = int(input("Enter the percent:"))
total_price = price + (price*percent)/100
percent_count = (price*percent)/100
print(percent_count,"\n",total_price)