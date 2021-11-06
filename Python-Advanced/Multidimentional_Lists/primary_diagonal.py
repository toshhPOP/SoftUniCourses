num = int(input())
matrix = [[int(x) for x in input().split()] for i in range(num)]
print(sum(matrix[i][i] for i in range(num)))
print(sum(matrix[i][num-i-1] for i in range(num)))
