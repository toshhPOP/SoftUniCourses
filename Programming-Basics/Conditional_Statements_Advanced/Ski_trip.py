days_stay = int(input())
room_type = input()
score = input()
nights = days_stay - 1
if room_type == "room for one person":
    price = 18 * nights
elif room_type == "apartment":
    price = 25 * nights
    if nights < 10:
        price -= 0.3 * price
    elif 10 <= nights <= 15:
        price -= 0.35 * price
    elif nights > 15:
        price -= 0.5 * price
elif room_type == "president apartment":
    price = 35 * nights
    if nights < 10:
        price -= 0.1 * price
    elif 10 <= nights <= 15:
        price -= 0.15 * price
    elif nights > 15:
        price -= 0.2 * price
if score == "positive":
    price += 0.25*price
elif score == "negative":
    price -= 0.1 * price
print(f"{price:.2f}")