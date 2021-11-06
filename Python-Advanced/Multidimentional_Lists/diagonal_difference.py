num = int(input())
matrix = [[int(x) for x in input().split()] for i in range(num)]
primary = [matrix[num-num+i][num-num+i] for i in range(num)]
secondary = [matrix[num-num+j][num-1-j] for j in range(num)]
print(abs(sum(primary)-sum(secondary)))