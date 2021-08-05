#!/usr/bin/env paython3

number_of_containers_of_one_liter_or_less = float(input("Enter number of one liter or less containers: "))
number_of_containers_holding_more_than_one_liter = float(input("Enter number of more than one liter or containers: "))

deposit_for_one_liter_or_less = 0.10
deposit_for_more_than_one_liter = 0.25

print("Total refund for one liter or less containers: ","$", number_of_containers_of_one_liter_or_less*deposit_for_one_liter_or_less,)
print("Total refund for more than one liter containers: ","$", number_of_containers_holding_more_than_one_liter*deposit_for_more_than_one_liter)
