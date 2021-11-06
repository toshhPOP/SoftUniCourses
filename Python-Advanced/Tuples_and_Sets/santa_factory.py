dolls = 0
wooden_train = 0
teddy_bear = 0
bicycle = 0
from collections import deque

materials_box = [int(x) for x in input().split() if int(x) != 0]
magic = deque(int(x) for x in input().split() if int(x) != 0)
presents = {}
while materials_box:
    match = False
    if magic:
        current_material = materials_box.pop()
        current_magic = magic.popleft()
        result = current_magic * current_material
        if result < 0:
            total = current_material + current_magic
            if not total == 0:
                materials_box.append(current_material + current_magic)
        elif result == 150:
            dolls += 1
            toy = "Doll"
            if toy not in presents:
                presents[toy] = 0
            presents[toy] += 1
            match = True
        elif result == 250:
            wooden_train += 1
            toy = "Wooden train"
            if toy not in presents:
                presents[toy] = 0
            presents[toy] += 1
            match = True
        elif result == 300:
            teddy_bear += 1
            toy = "Teddy bear"
            if toy not in presents:
                presents[toy] = 0
            presents[toy] += 1
            match = True
        elif result == 400:
            bicycle += 1
            toy = "Bicycle"
            if toy not in presents:
                presents[toy] = 0
            presents[toy] += 1
            match = True
        if not match and result >= 0:
            current_material += 15
            materials_box.append(current_material)
    else:
        break
if dolls >= 1 and wooden_train >= 1 or (teddy_bear >= 1 and bicycle >= 1):
    print("The presents are crafted! Merry Christmas!")
else:
    print("No presents this Christmas!")
if materials_box:
    print(f"Materials left: {', '.join(str(a) for a in materials_box[::-1])}")
if magic:
    print(f"Magic left: {', '.join(str(a) for a in magic)}")
for present, amount in sorted(presents.items()):
    print(f"{present}: {amount}")
