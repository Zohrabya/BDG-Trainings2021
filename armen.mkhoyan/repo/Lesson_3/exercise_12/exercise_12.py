#!/usr/bin/env paython3

number_of_containers_of_one_liter_or_less = float(input("Enter number of one liter or less containers: "))
number_of_containers_holding_more_than_one_liter = float(input("Enter number of more than one liter or containers: "))

DEPOSIT_FOR_ONE_LITER_OR_LESS = 0.10
DEPOSIT_FOR__MORE_THAN_ONE_LITER = 0.25

#print("Total refund for one liter or less containers: ","$", round(number_of_containers_of_one_liter_or_less * DEPOSIT_FOR_ONE_LITER_OR_LESS, 2))
#print("Total refund for more than one liter containers: ","$", round(number_of_containers_holding_more_than_one_liter * DEPOSIT_FOR__MORE_THAN_ONE_LITER, 2))

print("Total refound is: ", "$", round((number_of_containers_of_one_liter_or_less * DEPOSIT_FOR_ONE_LITER_OR_LESS) + (number_of_containers_holding_more_than_one_liter * DEPOSIT_FOR__MORE_THAN_ONE_LITER), 2))
