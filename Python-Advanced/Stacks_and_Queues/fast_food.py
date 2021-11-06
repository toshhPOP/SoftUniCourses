from collections import deque

food = int(input())
queue = deque(int(x) for x in input().split())
print(max(queue))
while queue:
    order = queue.popleft()
    if order <= food:
        food -= order
    else:
        queue.appendleft(order)
        print(f"Orders left: {' '.join(str(a) for a in queue)}")
        exit()
print("Orders complete")
