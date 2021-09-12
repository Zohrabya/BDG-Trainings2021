price = float(input ("Enter price of the meal: "))
tax_Precent = 22
tip_Precent = 18
tip_value = price * 18 / 100
tax_value = price * 22 / 100
total_value = price + tip_value + tax_value

print("total value is equal: " + "{:.2f}".format(total_value))
print("tip value is equal: " + "{:.2f}".format(tip_value))
print("tax value is equal: " + "{:.2f}".format(tax_value))
