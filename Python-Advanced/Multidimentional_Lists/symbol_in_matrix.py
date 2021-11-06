n = int(input())
matrix = [[a for a in input().split()] for i in range(n)]
symbol = input()
founded = False
for i in range(n):
    current_list = [a for a in matrix[i]]
    for j in current_list:
        if symbol in j:
            index = j.index(symbol)
            founded = True
            print(f"({i}, {j.index(symbol)})")
            exit()
print(f"{symbol} does not occur in the matrix")