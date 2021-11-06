from collections import deque

customers = deque(int(x) for x in input().split(', '))
taxi = [int(x) for x in input().split(', ')]
total_time = 0

while customers and taxi:
    current_customer = customers.popleft()
    car = taxi.pop()
    if current_customer <= car:
        total_time += current_customer
    else:
        customers.appendleft(current_customer)
if not customers:
    print('All customers were driven to their destinations')
    print(f'Total time: {total_time} minutes')
else:
    print('Not all customers were driven to their destinations')
    print(f'Customers left: {", ".join(str(a) for a in customers)}')
