items = input().split("|")
budget = int(input())
new_price = 0
new_price_list = []
profit = 0
for item in items:
    type, price = item.split("->")
    price = float(price)
    if type == 'Clothes' and price > 50:
        continue
    elif type == 'Shoes' and price > 35:
        continue
    elif type == 'Accessories' and price > 35:
        continue
    if price <= budget:
        budget -= price
        new_price = price + 0.4 * price
        new_price_list.append(new_price)
        profit += new_price - price
for price in new_price_list:
    print(f"{price:.2f}", end=" ")
print()
print(f"Profit: {profit:.2f}")
if budget + sum(new_price_list) >= 150:
    print("Hello, France!")
else:
    print("Time to go.")
