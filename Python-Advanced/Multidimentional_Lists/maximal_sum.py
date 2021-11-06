def read_matrix():
    n, m = [int(x) for x in input().split()]
    matrix = [[int(x) for x in input().split()] for i in range(n)]
    return matrix


matrix = read_matrix()
n = len(matrix)
m = len(matrix[n - 1])
best = 0
for r in range(n - 2):
    for c in range(m - 2):
        line = [matrix[r][c], matrix[r][c + 1], matrix[r][c + 2]]
        line_1 = [matrix[r + 1][c], matrix[r + 1][c + 1], matrix[r + 1][c + 2]]
        line_2 = [matrix[r + 2][c], matrix[r + 2][c + 1], matrix[r + 2][c + 2]]
        new_matrix = []
        new_matrix.append(line)
        new_matrix.append(line_1)
        new_matrix.append(line_2)
        total = sum(a for sublist in new_matrix for a in sublist)
        if total > best:
            best = total
            best_matrix = new_matrix
print(f"Sum = {best}")
for i in range(len(best_matrix)):
    print(' '.join(str(a) for a in best_matrix[i]))
'''
def read_matrix():
    n, m = [int(x) for x in input().split()]
    matrix = [[int(x) for x in input().split()] for i in range(n)]
    return matrix


matrix = read_matrix()
rows = len(matrix)
cols = len(matrix[rows - 1])

best = - 999999
for row in range(rows - 2):
    for col in range(cols - 2):
        total = 0
        sub_matrix = []
        row_counter = 0
        for r in range(row, row + 3):
            sub_matrix.append([])
            for c in range(col, col + 3):
                sub_matrix[row_counter].append(matrix[r][c])
                total += matrix[r][c]
            row_counter += 1
        if total > best:
            best = total
            best_matrix = sub_matrix
print(f"Sum = {best}")
for row in best_matrix:
    print(' '.join(str(a) for a in row))
'''
