products = {}
while True:
    command = input().split(": ")
    if command[0] == "statistics":
        break
    product = command[0]
    if product in products:
        products[product] += int(command[1])
        continue
    value = command[1]
    products[product] = int(value)
print("Products in stock:")
for product, quantity in products.items():
    print(f"- {product}: {quantity}")
print(f"Total Products: {len(products.keys())}")
print(f"Total Quantity: {sum(products.values())}")
