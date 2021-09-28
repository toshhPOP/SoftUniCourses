budget = float(input())
kg_flour_price = float(input())
eggs_price = 0.75*kg_flour_price
milk_l = (125*kg_flour_price)/100
price_for_one_cozonac = kg_flour_price + eggs_price + milk_l/4
counter = 0
colored_eggs = 0
while budget - price_for_one_cozonac > 0:
    budget -= price_for_one_cozonac
    counter += 1
    colored_eggs += 3
    if counter % 3 == 0:
        colored_eggs -= (counter - 2)
print(f"You made {counter} cozonacs! Now you have {colored_eggs} eggs and {budget:.2f}BGN left.")
