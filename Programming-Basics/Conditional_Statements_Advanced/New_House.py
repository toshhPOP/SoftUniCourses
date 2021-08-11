flower = input()
flowers_quantyty = int(input())
budget = int(input())
price = 0
if flower == "Roses":
    price = 5 * flowers_quantyty
    if flowers_quantyty > 80:
        price -= 0.1 * price
elif flower == "Dahlias":
    price = 3.80 * flowers_quantyty
    if flowers_quantyty > 90:
        price -= 0.15 * price
elif flower == "Tulips":
    price = 2.8 * flowers_quantyty
    if flowers_quantyty > 80:
        price -= 0.15 * price
elif flower == "Narcissus":
    price = 3 * flowers_quantyty
    if flowers_quantyty < 120:
        price += 0.15 * price
elif flower == "Gladiolus":
    price = 2.5 * flowers_quantyty
    if flowers_quantyty < 80:
        price += 0.2 * price
if budget >= price:
    diff = budget - price
    print(f"Hey, you have a great garden with {flowers_quantyty} {flower} and {diff:.2f} leva left.")
else:
    diff = price - budget
    print(f"Not enough money, you need {diff:.2f} leva more.")
