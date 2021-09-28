events = input().split("|")
energy = 100
coins = 100
for event in events:
    action, value = event.split("-")
    if action == "rest":
        energy += int(value)
        if energy > 100:
            energy -= int(value)
            print(f"You gained 0 energy.\nCurrent energy: {energy}.")
        else:
            print(f"You gained {value}energy.\nCurrent energy: {energy}.")
    elif action == "order":
        energy -= 30
        if energy < 0:
            print(f"You had to rest!")
            energy += 50
            continue
        else:
            coins += int(value)
            print(f"You earned {int(value)} coins.")
    else:
        coins -= int(value)
        if coins >= 0:
            print(f"You bought {action}.")
        else:
            print(f"Closed! Cannot afford {action}.")
            exit()
print("Day completed!")
print(f"Coins: {coins}")
print(f"Energy: {energy}")
