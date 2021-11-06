def valid_coordinates(size, r, c):
    size = len(field)
    if r >= 0 and c >= 0 and r < size and c < size:
        return r, c
    return False


def check_surroundings(r, c):
    bombs = 0
    if valid_coordinates(size, r, c + 1):
        if field[r][c + 1] == '*':
            bombs += 1
    if valid_coordinates(size, r, c - 1):
        if field[r][c - 1] == '*':
            bombs += 1
    if valid_coordinates(size,r-1,c):
        if field[r-1][c] == '*':
            bombs += 1
    if valid_coordinates(size, r + 1, c):
        if field[r + 1][c] == '*':
            bombs += 1
    if valid_coordinates(size, r + 1, c + 1):
        if field[r + 1][c + 1] == '*':
            bombs += 1
    if valid_coordinates(size, r + 1, c - 1):
        if field[r + 1][c - 1] == '*':
            bombs += 1
    if valid_coordinates(size, r - 1, c + 1):
        if field[r - 1][c + 1] == '*':
            bombs += 1
    if valid_coordinates(size, r - 1, c - 1):
        if field[r - 1][c - 1] == '*':
            bombs += 1
    return bombs


size = int(input())
mines_count = int(input())

field = [['' for i in range(size)] for a in range(size)]
for e in range(mines_count):
    line = input()
    line = line.strip('(')
    line = line.strip(')')
    mr = int(line.split(', ')[0])
    mc = int(line.split(', ')[1])
    field[mr][mc] = '*'
for r in range(size):
    for c in range(size):
        if field[r][c] == '*':
            continue
        field[r][c] = check_surroundings(r, c)
for el in field:
    print(' '.join([str(a) for a in el]))


########### VARIAN 2 ###########
# def is_in_range(row, col, n):
#     if 0 <= row < n and 0 <= col < n:
#         return True
#     return False
#
#
# def check_for_mines(r, c):
#     for direction in directions:
#         next_row = r + directions[direction][0]
#         next_col = c + directions[direction][1]
#         if is_in_range(next_row, next_col, size):
#             if mine_field[next_row][next_col] == '*':
#                 mine_field[r][c] += 1
#     return mine_field
#
#
# def cell_value(row, col):
#     for r in range(size):
#         for c in range(size):
#             check_for_mines(r, c)
#
# def field(size):
#     mine_field = [[0 for i in range(size)] for _ in range(size)]
#     return mine_field
#
# def mines(bombs):
#     mines = []
#     for i in range(bombs):
#         line = input()
#         coordinates = [int(x) for x in line[1:-1].split(', ')]
#         x, y = coordinates[0], coordinates[1]
#         mines.append([x, y])
#     return mines
#
# def place_mines(mine_field):
#     for m in mines:
#         mine_field[m[0]][m[1]] = '*'
#     return mine_field
# size = int(input())
# bombs = int(input())
#
# directions = {
#     'up': (-1, 0),
#     'down': (1, 0),
#     'left': (0, -1),
#     'right': (0, 1),
#     'up_right': (-1, 1),
#     'up_left': (-1, -1),
#     'down_right': (1, 1),
#     'down_left': (1, -1)
# }
# mine_field = field(size)
# mines = mines(bombs)
# mine_field = place_mines(mine_field)
# for r in range(size):
#     for c in range(size):
#         if mine_field[r][c] != '*':
#             check_for_mines(r, c)
# for f in mine_field:
#     print(' '.join([str(a) for a in f]))
