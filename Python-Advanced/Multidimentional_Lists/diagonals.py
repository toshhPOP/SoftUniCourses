# num = int(input())
# matrix = [[int(x) for x in input().split(', ')] for i in range(num)]
# primary = [matrix[i][i] for i in range(num)]
# secondary = [matrix[j][num-1-j] for j in range(num)]
# print(f"Primary diagonal: {', '.join(str(a) for a in primary)}. Sum: {sum(primary)}")
# print(f"Secondary diagonal: {', '.join(str(a) for a in secondary)}. Sum: {sum(secondary)}")

num = int(input())
matrix = [[int(x) for x in input().split(', ')] for i in range(num)]
primary = []
secondary = []
for i in range(num):
    diagonal = matrix[i][i]
    primary.append(diagonal)
for j in range(num):
    diagonal = matrix[j][num-1-j]
    secondary.append(diagonal)