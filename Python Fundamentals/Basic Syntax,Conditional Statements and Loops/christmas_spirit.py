quantity = int(input())
days = int(input())
ornament_set = 2
tree_skirt = 5
tree_garlands = 3
tree_lights = 15
total_cost = 0
spirit_points = 0
last_day = 0
for i in range(1,days +1):
    if i % 11 == 0:
        quantity += 2
    if i % 2 == 0:
        total_cost += quantity*ornament_set
        spirit_points += 5
    if i % 3 == 0:
        total_cost += quantity*tree_skirt + quantity*tree_garlands
        spirit_points += 13
    if i % 5 == 0:
        total_cost += quantity*tree_lights
        spirit_points += 17
        if i % 3 == 0:
            spirit_points += 30
    if i % 10 == 0:
        total_cost += tree_lights + tree_garlands + tree_skirt
        spirit_points -= 20
    if i == days:
        last_day = days
        if last_day % 10 == 0:
            spirit_points -= 30
print(f'Total cost: {total_cost}')
print(f'Total spirit: {spirit_points}')