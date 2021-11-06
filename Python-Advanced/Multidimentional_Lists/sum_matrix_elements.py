matrix = []
rows, column = input().split(', ')
for i in range(int(rows)):
    matrix.append([])
    numbers = [int(x) for x in input().split(', ')]
    for j in range(int(column)):
        matrix[i].append(numbers[j])
total = 0
for el in matrix:
    total += sum(el)
print(total)
print(matrix)
print(matrix[0][0])
