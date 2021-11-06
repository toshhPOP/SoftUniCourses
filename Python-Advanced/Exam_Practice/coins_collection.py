import math

def valid_position(matrix, r, c):
    matrix = size
    if r >= 0 and c >= 0 and r < size and c < size:
        return True
    return False

def valid_direction(command):
    if command not in ['up','down','left','right']:
        return False
    return True
def next_move(command):
    if command == 'up':
        if valid_position(size, player[0] - 1, player[1]):
            player_position = [player[0] - 1, player[1]]
            return player_position
    elif command == 'down':
        if valid_position(size, player[0] + 1, player[1]):
            player_position = [player[0] + 1, player[1]]
            return player_position
    elif command == 'right':
        if valid_position(size, player[0], player[1] + 1):
            player_position = [player[0], player[1] + 1]
            return player_position
    elif command == 'left':
        if valid_position(size, player[0], player[1] - 1):
            player_position = [player[0], player[1] - 1]
            return player_position
collected = False
game_over = False
coins = 0
size = int(input())
matrix = [[x for x in input().split()] for i in range(size)]
for r in range(size):
    for c in range(size):
        if matrix[r][c] == 'P':
            player = [r, c]
path = []
command = input()
while command != '':
    if not valid_direction(command):
        command = input()
        continue
    player = next_move(command)
    if not player or matrix[player[0]][player[1]] == 'X':
        game_over = True
        break
    if matrix[player[0]][player[1]].isdigit():
        coins += int(matrix[player[0]][player[1]])
        path.append(player)
        if coins >= 100:
            collected = True
            break
    command = input()
if game_over:
    print(f"Game over! You've collected {math.floor(coins/2)} coins.")
if collected:
    print(f"You won! You've collected {math.floor(coins)} coins.")
print('Your path:')
for p in path:
    print(p)
