from collections import  deque
queue = deque()
while True:
    name = input()
    if name == "Paid":
        while len(queue) > 0:
            print(queue.popleft())
    elif name == "End":
        break
    else:
        queue.append(name)
print(f"{len(queue)} people remaining.")