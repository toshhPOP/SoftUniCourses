def is_knight_placed(board, r, c):
    board_size = len(board)
    if r < 0 or c < 0 or r >= board_size or c >= board_size:
        return False
    return board[r][c] == "K"


def count_affected_knights(board, r, c):
    result = 0
    board_size = len(board)
    if is_knight_placed(board, r - 2, c - 1):
        result += 1
    if is_knight_placed(board, r - 2, c + 1):
        result += 1
    if is_knight_placed(board, r + 2, c - 1):
        result += 1
    if is_knight_placed(board, r + 2, c + 1):
        result += 1
    if is_knight_placed(board, r - 1, c - 2):
        result += 1
    if is_knight_placed(board, r - 1, c + 2):
        result += 1
    if is_knight_placed(board, r + 1, c - 2):
        result += 1
    if is_knight_placed(board, r + 1, c + 2):
        result += 1
    return result


size = int(input())
matrix = [[x for x in input()] for i in range(size)]
removed_knights = 0
while True:
    max_count = 0
    knight_row, knight_col = 0, 0
    for r in range(size):
        for c in range(size):
            if matrix[r][c] == '0':
                continue
            count = count_affected_knights(matrix, r, c)
            if count > max_count:
                max_count, knight_row, knight_col = count, r, c
    if max_count == 0:
        break
    matrix[knight_row][knight_col] = '0'
    removed_knights += 1
print(removed_knights)
