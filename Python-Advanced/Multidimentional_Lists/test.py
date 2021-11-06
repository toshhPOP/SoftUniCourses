def valid_position(size, r, c):
    if 0 <= r < size and 0 <= c < size:
        return True
    return False


def next_position(direction, r, c, steps):
    if direction == 'up':
        if valid_position(size, r - steps, c):
            player_position = [r - steps, c]
            return player_position
        return False
    elif direction == 'down':
        if valid_position(size, r + steps, c):
            player_position = [r + steps, c]
            return player_position
        return False
    elif direction == 'right':
        if valid_position(size, r, c + steps):
            player_position = [r, c + steps]
            return player_position
        return False
    elif direction == 'left':
        if valid_position(size, r, c - steps):
            player_position = [r, c - steps]
            return player_position
        return False


def shooting(direction, r, c):
    if direction == 'up':
        if valid_position(size, r - 1, c):
            for row in range(r, -1, -1):
                if shooting_gallery[row][c] == 'x':
                    targets.append([row, c])
                    shooting_gallery[row][c] = '.'
                    return targets

    elif direction == 'down':
        if valid_position(size, r + 1, c):
            for row in range(r, size + 1):
                if shooting_gallery[row][c] == 'x':
                    targets.append([row, c])
                    shooting_gallery[row][c] = '.'
                    return targets


    elif direction == 'right':
        if valid_position(size, r, c + 1):
            for col in range(c, size + 1):
                if shooting_gallery[r][col] == 'x':
                    targets.append([r, col])
                    shooting_gallery[r][col] = '.'
                    return targets

    elif direction == 'left':
        if valid_position(size, r, c - 1):
            for col in range(c, -1, -1):
                if shooting_gallery[r][col] == 'x':
                    targets.append([r, col])
                    shooting_gallery[r][col] = '.'
                    return targets


shooting_gallery = [[x for x in input().split()] for _ in range(5)]
commands = int(input())
size = len(shooting_gallery)
targets = []
total_targets = []
for r in range(size):
    for c in range(size):
        if shooting_gallery[r][c] == 'A':
            player_position = [r, c]
        elif shooting_gallery[r][c] == 'x':
            total_targets.append([r, c])
pr = player_position[0]
pc = player_position[1]

for _ in range(commands):
    command = input().split()
    action = command[0]
    direction = command[1]
    if action == 'shoot':
        if valid_position(size, pr, pc):
            shooting(direction, pr, pc)
    elif action == 'move':
        steps = int(command[2])
        player_position = next_position(direction, pr, pc, steps)
        if not player_position:
            continue
        else:
            if shooting_gallery[player_position[0]][player_position[1]] == '.':
                shooting_gallery[pr][pc] = '.'
                pr = player_position[0]
                pc = player_position[1]
                shooting_gallery[pr][pc] = 'A'
if len(targets) < len(total_targets):
    print(f"Training not completed! {len(total_targets) - len(targets)} targets left.")
else:
    print(f"Training completed! All {len(targets)} targets hit.")
for t in targets:
    print(t)
