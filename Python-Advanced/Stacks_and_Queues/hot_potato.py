from collections import deque

kids = deque(input().split())
counter = 0
toss = int(input())
# while len(kids) > 1:
#     kids.append(kids.popleft())
#     counter += 1
#     if counter == toss:
#         print(f"Removed {kids.pop()}")
#         counter = 0
# print(f"Last is {''.join(kids)}")
while len(kids) > 1:
    kids.rotate(-toss)
    print(f"Removed {kids.pop()}")
print(f"Last is {''.join(kids)}")