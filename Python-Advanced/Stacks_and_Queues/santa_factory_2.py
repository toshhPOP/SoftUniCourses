from collections import deque

boxes = [int(x) for x in input().split()]
magic = deque(int(x) for x in input().split())
presents = {
    150: "Doll",
    250: "Wooden train",
    300: "Teddy bear",
    400: "Bicycle"
}
crafted_presents = {}
while boxes and magic:
    box = boxes.pop()
    magic_value = magic.popleft()
    result = box * magic_value

    if box == 0 and magic_value == 0:
        continue
    if box == 0:
        magic.appendleft(magic_value)
        continue
    if magic_value == 0:
        boxes.append(box)

    if result < 0:
        boxes.append(box + magic_value)

    elif result in presents:
        pass
        present = presents[result]
        if present in crafted_presents:
            crafted_presents[present] += 1
        else:
            crafted_presents[present] = 1
    else:
        boxes.append(box + 15)
is_done = ('Doll' in crafted_presents and "Wooden train" in crafted_presents) or\
          ('Teddy bear' in crafted_presents and 'Bicycle' in crafted_presents)
if is_done:
    print("The presents are crafted! Merry Christmas!")
else:
    print("No presents this Christmas!")
if boxes:
    print(f"Materials left: {', '.join(str(a) for a in boxes[::-1])}")
if magic:
    print(f"Magic left: {', '.join(str(a) for a in magic)}")
for present, amount in sorted(presents.items()):
    print(f"{present}: {amount}")