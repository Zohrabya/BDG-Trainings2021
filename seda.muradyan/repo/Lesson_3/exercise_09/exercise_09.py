price = float(input ("Enter price of the meal: "))
tip_pracent = float(input ("Enter tip percent: "))

tip_value = price * tip_pracent / 100
total_value = price + tip_value

print("total value is equal " + str(total_value))
print("tip value is equal " + str(tip_value))