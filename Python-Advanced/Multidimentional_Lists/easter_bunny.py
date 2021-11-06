from collections import deque

n = int(input())
matrix = [[x for x in input().split()] for i in range(n)]

directions = {}
for r in range(n):
    for c in range(n):
        if matrix[r][c] == "B":
            bunny_position = [r, c]

max_eggs = 0
list_directions = deque(['up', 'down', 'left', 'right'])
while list_directions:
    eggs = 0
    path = []
    new_row = bunny_position[0]
    new_col = bunny_position[1]
    step = list_directions.popleft()
    if step == 'up':
        for i in range(n):
            new_row -= 1
            if new_row >= 0 :
                current_position = [new_row,new_col]
                if matrix[current_position[0]][current_position[1]] != 'X':
                    eggs += int(matrix[current_position[0]][current_position[1]])
                    path.append(current_position)
                else:
                    break
            else:
                break
    elif step == 'down':
        for i in range(n):
            new_row += 1
            if new_row < n:
                current_position = [new_row,new_col]
                if matrix[current_position[0]][current_position[1]] != 'X':
                    eggs += int(matrix[current_position[0]][current_position[1]])
                    path.append(current_position)
                else:
                    break
            else:
                break
    elif step == 'left':
        for i in range(n):
            new_col -= 1
            if new_col > 0:
                current_position = [new_row,new_col]
                if matrix[current_position[0]][current_position[1]] != 'X':
                    eggs += int(matrix[current_position[0]][current_position[1]])
                    path.append(current_position)
                else:
                    break
            else:
                break
    elif step == 'right':
        for i in range(n):
            new_col += 1
            if new_col < n:
                current_position = [new_row,new_col]
                if matrix[current_position[0]][current_position[1]] != 'X':
                    eggs += int(matrix[current_position[0]][current_position[1]])
                    path.append(current_position)
                else:
                    break
            else:
                continue
    if eggs >= max_eggs:
        max_eggs = eggs
        max_step = step
        max_path = path
print(max_step)
for i in max_path:
    print(i)
print(max_eggs)
