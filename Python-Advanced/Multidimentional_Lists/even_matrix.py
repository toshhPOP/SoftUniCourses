rows = int(input())
matrix = [[int(x) for x in input().split(', ')] for _ in range(rows)]
even_matrix = []
for el in matrix:
    only_even = [x for x in el if x % 2 == 0]
    even_matrix.append(only_even)
print(even_matrix)
