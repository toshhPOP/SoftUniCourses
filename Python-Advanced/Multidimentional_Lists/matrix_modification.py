n = int(input())
matrix = [[int(x) for x in input().split()] for i in range(n)]
while True:
    command = input()
    if command == "END":
        break
    action, row, col, value = command.split()
    row = int(row)
    col = int(col)
    value = int(value)
    if row in range(0, len(matrix)) and col in range(0, len(matrix)):
        if action == "Add":
            matrix[row][col] += value
        elif action == "Subtract":
            matrix[row][col] -= value
    else:
        print("Invalid coordinates")
for el in matrix:
    print(' '.join(str(a) for a in el))
