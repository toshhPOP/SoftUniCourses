from collections import deque

rows, cols = [int(x) for x in input().split()]
text = deque(input())

matrix = []

for row in range(rows):
    matrix.append([])
    for col in range(cols):
        matrix[row].append('')
for row in range(rows):
    if row % 2 == 0:
        for col in range(cols):
            letter = text.popleft()
            matrix[row][col] += letter
            text.append(letter)
        print(''.join(a for a in matrix[row]))

    else:
        for col in range(cols, 0, -1):
            current_col = col - 1
            letter = text.popleft()
            matrix[row][current_col] += letter
            text.append(letter)
        print(''.join(a for a in matrix[row]))
