liter_or_less = int(input("Enter bottles (1 liter or less) liter: "))
more_than_liter = int(input("Enter bottles ( more than) liter: "))
total = (0.10 * liter_or_less) + (0.25 * more_than_liter)

print("$" + "{:.2f}".format(total))