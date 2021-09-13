#!/usr/bin/evn python3

new_price_list = []
discount_amounts_list = []
purchases_list = [4.95, 9.95, 14.95, 19.95, 24.95]
percent_of_sale = 0.6
index = 0
for element in purchases_list:
    discount_amount = element * percent_of_sale
    discount_amounts_list += [round(discount_amount, 2)]
for element in purchases_list:
    new_price = purchases_list[index] - discount_amounts_list[index]
    new_price_list += [round(new_price, 2)]
    index += 1
print("Original price: ", purchases_list)
print("Discount amount:", discount_amounts_list)
print("New price:\t", new_price_list)
