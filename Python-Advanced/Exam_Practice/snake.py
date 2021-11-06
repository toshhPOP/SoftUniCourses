def valid(size, r, c):
    if r >= 0 and c >= 0 and r < size and c < size:
        snake_row = r
        snake_col = c
        snake_position = [snake_row, snake_col]
        return snake_position
    return False


size = int(input())
matrix = [[x for x in input()] for i in range(size)]
burrows = []
food = 0
path = []
for r in range(size):
    for c in range(size):
        if matrix[r][c] == 'S':
            snake_position = [r, c]
        elif matrix[r][c] == 'B':
            burrows.append([r, c])
snake_row = snake_position[0]
snake_col = snake_position[1]
path.append([snake_row, snake_col])
directions = ["up", "down", "left", "right"]
game_over = False
fet_snake = False
while True:
    line = input()
    matrix[snake_row][snake_col] = '.'
    if line == 'up':
        snake_position = valid(size, snake_row - 1, snake_col)
        if snake_position:
            snake_row = snake_position[0]
            snake_col = snake_position[1]
    elif line == 'down':
        snake_position = valid(size, snake_row + 1, snake_col)
        if snake_position:
            snake_row = snake_position[0]
            snake_col = snake_position[1]
    elif line == 'left':
        snake_position = valid(size, snake_row, snake_col - 1)
        if snake_position:
            snake_row = snake_position[0]
            snake_col = snake_position[1]
    elif line == 'right':
        snake_position = valid(size, snake_row, snake_col + 1)
        if snake_position:
            snake_row = snake_position[0]
            snake_col = snake_position[1]
    if matrix[snake_row][snake_col] == '*':
        food += 1
        if food >= 10:
            matrix[snake_row][snake_col] = 'S'
            fet_snake = True
            break
    elif matrix[snake_row][snake_col] == 'B':
        matrix[snake_row][snake_col] = '.'
        snake_position = burrows[1]
        snake_row = snake_position[0]
        snake_col = snake_position[1]
        matrix[snake_row][snake_col] = '.'
    elif not snake_position:
        game_over = True
        matrix[snake_row][snake_col] = '.'
        break
if game_over:
    print("Game over!")
elif fet_snake:
    print("You won! You fed the snake.")
print(f"Food eaten: {food}")
for m in matrix:
    print(''.join(m))
