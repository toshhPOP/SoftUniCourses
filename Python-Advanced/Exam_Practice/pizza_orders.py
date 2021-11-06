orders = [int(x) for x in input().split(", ")]
employees = [int(x) for x in input().split(", ")]
total = 0
orders = orders[::-1]
while len(orders) > 0:
    pizza = orders.pop()
    if pizza > 10 or pizza <= 0:
        continue
    else:
        if len(employees) > 0:
            worker = employees.pop()
            if pizza > worker:
                pizza_left = pizza - worker
                total += pizza - pizza_left
                if len(employees) > 0:
                    worker = employees.pop()
                    if pizza_left <= worker:
                        total += pizza_left
                else:
                    orders.append(pizza_left)
                    print(f"Not all orders are completed.")
                    print(f"Orders left: {', '.join([str(a) for a in orders[::-1]])}")
                    exit()
            else:
                total += pizza
if len(employees) > 0:
    print('All orders are successfully completed!')
    print(f"Total pizzas made: {total}")
    print(f"Employees: {', '.join([str(a) for a in employees])}")
