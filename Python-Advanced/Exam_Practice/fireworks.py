from collections import deque

effects = deque(int(x) for x in input().split(", ") if int(x) > 0)
explosive_power = deque(int(x) for x in input().split(", ") if int(x) > 0)
is_ready = False
palm = 0
willow = 0
crossette = 0

while effects:
    if not explosive_power:
        break
    firework = effects.popleft()
    power = explosive_power.pop()
    sum = firework + power

    if sum % 3 == 0 and sum % 5 != 0:
        palm += 1
    elif sum % 5 == 0 and sum % 3 != 0:
        willow += 1
    elif sum % 3 == 0:
        crossette += 1
    else:
        firework -= 1
        if firework > 0:
            effects.append(firework)
        explosive_power.append(power)

    if palm >= 3 and willow >= 3 and crossette >= 3:
        is_ready = True
        break

if is_ready:
    print(f"Congrats! You made the perfect firework show!")
else:
    print("Sorry. You can't make the perfect firework show.")

if effects:
    print(f"Firework Effects left: {', '.join(str(a) for a in effects)}")
if explosive_power:
    print(f"Explosive Power left: {', '.join(str(a) for a in explosive_power)}")

print(f"Palm Fireworks: {palm}\n"
      f"Willow Fireworks: {willow}\n"
      f"Crossette Fireworks: {crossette}")