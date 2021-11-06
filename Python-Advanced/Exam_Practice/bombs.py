from collections import deque

bombs_effect = deque(int(x) for x in input().split(', '))
casing = [int(x) for x in input().split(', ')]
explosives = {
    40: 'Datura Bombs',
    60: 'Cherry Bombs',
    120: 'Smoke Decoy Bombs'
}
crafted_bombs = {
    'Datura Bombs': 0,
    'Cherry Bombs': 0,
    'Smoke Decoy Bombs': 0
}
while bombs_effect and casing:
    current_effect = bombs_effect.popleft()
    current_casing = casing.pop()
    result = current_casing + current_effect
    if result in explosives:
        crafted_bombs[explosives[result]] += 1
    else:
        casing.append(current_casing - 5)
        bombs_effect.appendleft(current_effect)
    for type_bomb, count in crafted_bombs.items():
        if count >= 3:
            fulfilled = True
        else:
            fulfilled = False
            break
    if fulfilled:
        break
if fulfilled:
    print("Bene! You have successfully filled the bomb pouch!")
else:
    print("You don't have enough materials to fill the bomb pouch.")
if bombs_effect:
    print(f"Bomb Effects: {', '.join((str(a) for a in bombs_effect))}")
else:
    print("Bomb Effects: empty")
if casing:
    print(f"Bomb Casings: {', '.join((str(a) for a in casing))}")
else:
    print("Bomb Casings: empty")
for type_bomb, count in sorted(crafted_bombs.items()):
    print(f"{type_bomb}: {count}")
