matrix = []
rows, column = input().split(', ')
rows = int(rows)
column = int(column)
for i in range(rows):
    matrix.append([])
    numbers = [int(x) for x in input().split()]
    for j in range(column):
        matrix[i].append(numbers[j])
result = 0
for i in range(column):
    for j in range(rows):
        result += matrix[j][i]
    print(result)
    result = 0

