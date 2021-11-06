def shopping_list(budget, **items):
    basket = 5
    products_bought = {}
    if not budget >= 100:
        return "You do not have enough budget."
    else:
        for product, values in items.items():
            total = float(values[0])*float(values[1])
            if budget > total:
                budget -= total
                if product not in products_bought:
                    products_bought[product] = total
                    basket -= 1
                    if basket == 0:
                        break
                else:
                    products_bought[product] += total
            else:
                continue
    result = ''
    if basket >= 0:
        for k, v in products_bought.items():
            result += f"You bought {k} for {v:.2f} leva.\n"
        return result



# print(shopping_list(100, microwave=(70, 2), skirts=(15, 4), coffee=(1.50, 10), ))
# print(shopping_list(20,
#                     jeans=(19.99, 1),
#                     ))
# print(shopping_list(104,
#                     cola=(1.20, 2),
#                     candies=(0.25, 15),
#                     bread=(1.80, 1),
#                     pie=(10.50, 5),
#                     tomatoes=(4.20, 1),
#                     milk=(2.50, 2),
#                     juice=(2, 3),
#                     eggs=(3, 1),
#                     ))

