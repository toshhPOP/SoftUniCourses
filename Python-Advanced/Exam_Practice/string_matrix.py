def valid_move(size, r, c):
    if 0 <= r < size and 0 <= c < size:
        return True
    return False


def next_position(command, pr, pc):
    if command == 'up':
        if valid_move(size, player_row - 1, player_col):
            new_position = [player_row - 1, player_col]
            return new_position
        return False
    elif command == 'down':
        if valid_move(size, player_row + 1, player_col):
            new_position = [player_row + 1, player_col]
            return new_position
        return False
    elif command == 'right':
        if valid_move(size, player_row, player_col + 1):
            new_position = [player_row, player_col + 1]
            return new_position
        return False

    elif command == 'left':
        if valid_move(size, player_row, player_col - 1):
            new_position = [player_row, player_col - 1]
            return new_position
        return False


text = input()
size = int(input())
field = [[x for x in input()] for _ in range(size)]
moves = int(input())
for r in range(size):
    for c in range(size):
        if field[r][c] == 'P':
            player_position = [r, c]
            player_row, player_col = r, c

for move in range(moves):
    command = input()
    new_position = next_position(command, player_row, player_col)
    if new_position:
        field[player_row][player_col] = '-'
        player_row = new_position[0]
        player_col = new_position[1]
        if field[player_row][player_col] != '-':
            text += field[player_row][player_col]
            field[player_row][player_col] = 'P'
    else:
        text = text[:-1]
print(text)
for f in field:
    print(''.join(f))

################## Variant 2
'''
def matrix(size):
    matrix = [[a for a in input()] for _ in range(size)]
    return matrix


def is_in_range(row, col, n):
    return 0 <= row < n and 0 <= col < n



def get_player_position(matrix):
    for r in range(size):
        for c in range(size):
            if matrix[r][c] == 'P':
                pp = [r, c]
                return pp


def next_position(direction, pp):
    if direction == 'up':
        if is_in_range(pp[0] + directions[direction][0], pp[1], size):
            string_matrix[pp[0]][pp[1]] = '-'
            pp = [pp[0] + directions[direction][0], pp[1]]
        else:
            return False
    elif direction == 'down':
        if is_in_range(pp[0] + directions[direction][0], pp[1], size):
            string_matrix[pp[0]][pp[1]] = '-'
            pp = [pp[0] + directions[direction][0], pp[1]]
        else:
            return False
    elif direction == 'left':
        if is_in_range(pp[0], pp[1] + directions[direction][1], size):
            string_matrix[pp[0]][pp[1]] = '-'
            pp = [pp[0], pp[1] + directions[direction][1]]
        else:
            return False
    elif direction == 'right':
        if is_in_range(pp[0], pp[1] + directions[direction][1], size):
            string_matrix[pp[0]][pp[1]] = '-'
            pp = [pp[0], pp[1] + directions[direction][1]]
        else:
            return False
    return pp


directions = {
    'up': (-1, 0),
    'down': (1, 0),
    'left': (0, -1),
    'right': (0, 1)
}

string = input()
size = int(input())

string_matrix = matrix(size)
moves = int(input())
pp = get_player_position(string_matrix)
for m in range(moves):
    move = input()
    np = next_position(move, pp)
    if np:
        if string_matrix[np[0]][np[1]] != '-':
            string += string_matrix[np[0]][np[1]]
            string_matrix[np[0]][np[1]] = 'P'
            pp = np
        else:
            string_matrix[np[0]][np[1]] = 'P'
            pp = np
    else:
        string = string[:-1]
print(string)
for i in string_matrix:
    print(''.join(i))

'''