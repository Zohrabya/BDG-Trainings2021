container_size = float(input("Please, enter size of the drink container (liter): "))
container_quantity = int(input("Please, enter quantity of drink containers which have that size:  "))
total_refund = 0

if 0 < container_size <= 1:
    deposit = 0.10
    total_refund += (deposit * container_quantity)
    print(f'Refund: {deposit}$. Your total refund is {total_refund}$')
elif container_size > 1:
    deposit = 0.25
    total_refund += (deposit * container_quantity)
    print(f'Refund: {deposit}$. Your total refund is {total_refund}$')
else:
    print("Something went wrong.")
