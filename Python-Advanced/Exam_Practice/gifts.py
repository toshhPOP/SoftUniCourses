from collections import deque


def check_present(total):
    total = total
    if 100 <= total <= 199:
        result = 'Gemstone'
    elif 200 <= total <= 299:
        result = 'Porcelain Sculpture'
    elif 300 <= total <= 399:
        result = 'Gold'
    elif 400 <= total <= 499:
        result = 'Diamond Jewellery'
    else:
        result = None
    return result


def check_success(gifts):
    if (gifts['Gemstone'] > 0 and gifts['Porcelain Sculpture'] > 0) or (gifts['Gold'] > 0 and gifts['Diamond Jewellery'] > 0):
        return True
    return False

gifts = {'Gemstone': 0,
         'Porcelain Sculpture': 0,
         'Gold': 0,
         "Diamond Jewellery": 0
         }
materials = [int(x) for x in input().split()]
magic_level = deque(int(x) for x in input().split())
success = False
while materials and magic_level:
    current_material = materials[-1]
    current_magic = magic_level[0]
    total = current_material + current_magic
    gift = check_present(total)
    if gift:
        gifts[gift] += 1
        success = check_success(gifts)
    else:
        if total < 100:
            if total % 2 == 0:
                total = current_material * 2 + current_magic * 3
            elif total % 2 != 0:
                total *= 2
        elif total > 499:
            total /= 2
        gift = check_present(total)
        if gift:
            gifts[gift] += 1
            success = check_success(gifts)
    if success:
        success = True
    materials.pop()
    magic_level.popleft()
if success:
    print("The wedding presents are made!")
else:
    print("Aladdin does not have enough wedding presents.")
if materials:
    print(f"Materials left: {', '.join(str(a) for a in materials)}")
if magic_level:
    print(f"Magic left: {', '.join(str(a) for a in magic_level)}")
for k,v in sorted(gifts.items()):
    if v > 0:
        print(f"{k}: {v}")