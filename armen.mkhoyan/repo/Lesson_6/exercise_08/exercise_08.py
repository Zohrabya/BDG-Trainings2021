#!usr/bin/evn python 3

PRACENT_OF_SALE = 60

new_price_list = [4.95, 9.95, 14.95, 19.95, 24.95]
product_price_list = []

for i in range(len(new_price_list)):
    product_price_list.append((new_price_list[i] * 100) / PRACENT_OF_SALE)

    
    print("The original price: ", round(product_price_list[i],2), " "*2, "The discount amount: ", round((product_price_list[i] - new_price_list[i]), 2), " "*2, "The new price: ", new_price_list[i])
