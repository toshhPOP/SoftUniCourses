trip_cost = float(input())
puzzles_count = int(input())
puppets_count = float(input())
bears_count = int(input())
minions_count = int(input())
trucks_count = int(input())
toys_count = puppets_count + puppets_count + bears_count + minions_count + trucks_count
total_income = puzzles_count*2.60 + puppets_count*3 + bears_count*4.10 + minions_count*8.20 +trucks_count*2
if toys_count >= 50:
    total_income -= 0.25*total_income
total_income -= 0.1*total_income
if total_income >= trip_cost:
    diff = total_income - trip_cost
    print(f"Yes! {diff:.2f} lv left.")
else:
    diff = trip_cost - total_income
    print(f"Not enough money! {diff:.2f} lv needed.")