meal_cost = float(input("Please, enter the cost of the meal: "))
cost_tax = meal_cost * 0.20
tip = meal_cost * 0.18
total_cost = meal_cost + cost_tax + tip

print(f'Tax: {cost_tax:.2f}$. Tip: {tip:.2f}. Total: {total_cost:.2f}$')
