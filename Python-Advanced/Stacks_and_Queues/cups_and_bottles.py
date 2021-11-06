from collections import deque

cup_capacity = deque(int(x) for x in input().split())
bottles = deque(int(x) for x in input().split())
wasted_litters = 0
while cup_capacity:
    if bottles:
        cup = cup_capacity.popleft()
        bottle = bottles.pop()
        if bottle >= cup:
            wasted_litters += bottle - cup
        elif bottle < cup:
            cup_capacity.appendleft(cup - bottle)
    else:
        break
if cup_capacity:
    print(f"Cups: {' '.join(str(a) for a in cup_capacity)}")
else:
    print(f"Bottles: {' '.join(str(a) for a in bottles)}")
print(f"Wasted litters of water: {wasted_litters}")
