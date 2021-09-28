products = input().split()
searched_products = input().split()
product_dict = {}
for i in range(0, len(products), 2):
    product = products[i]
    quantity = products[i + 1]
    product_dict[product] = int(quantity)
for product in searched_products:
    if product in product_dict:
        print(f"We have {product_dict[product]} of {product} left")
    else:
        print(f"Sorry, we don't have {product}")
