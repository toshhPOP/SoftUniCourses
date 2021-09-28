elements = input().split()
foods_dict = {}
for el in range(0,len(elements),2):
    food = elements[el]
    quantity = elements[el + 1]
    foods_dict[food] = int(quantity)
print(foods_dict)