def valid_move(size, r, c):
    size = len(matrix)
    if r >= 0 and c >= 0 and r < size and c < size:
        return True
    return False


def next_position(command):
    if command == 'up':
        if valid_move(size, player[0] - int(step), player[1]):
            player[0] -= int(step)
            if matrix[player[0]][player[1]] == '.':
                return player
        else:
            return False
    elif command == 'down':
        if valid_move(size, player[0] + int(step), player[1]):
            player[0] += int(step)
            if matrix[player[0]][player[1]] == '.':
                return player
        else:
            return False
    elif command == 'right':
        if valid_move(size, player[0], player[1] + int(step)):
            player[1] += int(step)
            if matrix[player[0]][player[1]] == '.':
                return player
        else:
            return False
    elif command == 'left':
        if valid_move(size, player[0], player[1] - int(step)):
            player[1] -= int(step)
            if matrix[player[0]][player[1]] == '.':
                return player
        else:
            return False
def shooting(command):
    if command == 'up':
        if valid_move(size, player[0] - 1, player[1]):
            for i in range(player[0] - 1, -1, -1):
                if matrix[i][player[1]] == 'x':
                    matrix[i][player[1]] = '.'
                    targets_down.append([i, player[1]])
                    break
        else:
            return False
    elif command == 'down':
        if valid_move(size, player[0] + 1, player[1]):
            for i in range(player[0] + 1, size):
                if matrix[i][player[1]] == 'x':
                    matrix[i][player[1]] = '.'
                    targets_down.append([i, player[1]])
                    break
        else:
            return False
    elif command == 'right':
        if valid_move(size, player[0], player[1] + 1):
            for i in range(player[1] + 1, size):
                if matrix[player[0]][i] == 'x':
                    matrix[player[0]][i] = '.'
                    targets_down.append([player[0], i])
                    break
        else:
            return False
    elif command == 'left':
        if valid_move(size, player[0], player[1] - 1):
            for i in range(player[1] - 1, -1, -1):
                if matrix[player[0]][i] == 'x':
                    matrix[player[0]][i] = '.'
                    targets_down.append([player[0], i])
                    break

        else:
            return False


all_down = False
targets_down = []
targets = 0
size = 5
matrix = [[x for x in input().split()] for i in range(size)]
for r in range(size):
    for c in range(size):
        if matrix[r][c] == 'A':
            player = [r, c]
        elif matrix[r][c] == 'x':
            targets += 1
moves = int(input())
for step in range(moves):
    command = input().split()
    if command[0] == 'move':
        direction, step = command[1:]
        if not next_position(direction):
            continue
        else:
            next_position(direction)
    elif command[0] == 'shoot':
        if shooting(command[1]) == False:
            continue
        else:
            targets -= len(targets_down)
            if targets <= 0:
                all_down = True
                break
if all_down:
    print(f"Training completed! All {len(targets_down)} targets hit.")
else:
    print(f"Training not completed! {targets} targets left.")
for p in targets_down:
    print(p)
