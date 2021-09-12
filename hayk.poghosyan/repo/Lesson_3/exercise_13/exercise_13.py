# 13
meal_cost = float(input("Enter the cost of a meal: "))
local_tax_rate_text = float(input("Enter the local tax rate: "))
tip = (meal_cost * 18)/100
local_tax_rate = (meal_cost * local_tax_rate_text)/100
total_cost = tip + local_tax_rate + meal_cost
print("Tip is: " + str(tip))
print("Local tax rate is: " + str(local_tax_rate))
print("Total cost is: " + str(total_cost))
