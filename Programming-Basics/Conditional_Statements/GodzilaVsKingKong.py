budget = float(input())
statists = int(input())
clothes = float(input())
decoration = 0.1 * budget
statists_expenses = statists * clothes
needed_money = decoration + statists_expenses
if statists >= 150:
    statists_expenses -= 0.1*statists_expenses
    needed_money = decoration + statists_expenses
if budget >= needed_money:
    diff = budget - needed_money
    print(f"Action!")
    print(f"Wingard starts filming with {diff:.2f} leva left.")
else:
    diff = needed_money - budget
    print("Not enough money!")
    print(f"Wingard needs {diff:.2f} leva more.")