def read_matrix():
    n, m = [int(x) for x in input().split()]
    matrix = [[x for x in input().split()] for i in range(n)]
    return matrix


matrix = read_matrix()
n = len(matrix)
m = len(matrix[n - 1])
counter = 0

for r in range(n - 1):
    for c in range(m - 1):
        square = []
        if matrix[r][c] == matrix[r][c + 1] == matrix[r + 1][c] == matrix[r + 1][c + 1]:
            counter += 1
        # square.append(matrix[r][c])
        # square.append(matrix[r][c + 1])
        # square.append(matrix[r + 1][c])
        # square.append(matrix[r + 1][c + 1])
        # for el in square:
        #     if square.count(el) == 4:
        #         counter += 1
        #         break
        #     else:
        #         break
print(counter)
