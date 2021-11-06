gifts = int(input())
size = int(input())
matrix = [[x for x in input().split()] for _ in range(size)]
nice = 0
for r in range(size):
    for c in range(size):
        if matrix[r][c] == 'S':
            santa = [r, c]
        elif matrix[r][c] == 'V':
            nice += 1


def valid_position(size, r, c):
    if r >= 0 and c >= 0 and r < size and c < size:
        return True
    return False


def movement(command):
    if command == 'up':
        if valid_position(size, santa[0] - 1, santa[1]):
            old = [santa[0], santa[1]]
            matrix[old[0]][old[1]] = '-'
            santa[0] -= 1
            return santa
    elif command == 'down':
        if valid_position(size, santa[0] + 1, santa[1]):
            old = [santa[0], santa[1]]
            matrix[old[0]][old[1]] = '-'
            santa[0] += 1
            return santa
    elif command == 'right':
        if valid_position(size, santa[0], santa[1] + 1):
            old = [santa[0], santa[1]]
            matrix[old[0]][old[1]] = '-'
            santa[1] += 1
            return santa
    elif command == 'left':
        if valid_position(size, santa[0], santa[1] - 1):
            old = [santa[0], santa[1]]
            matrix[old[0]][old[1]] = '-'
            santa[1] -= 1
            return santa

happy = 0
no_gifts = False
while True:
    command = input()
    if command == "Christmas morning" or gifts == 0:
        break
    santa = movement(command)
    if not santa:
        continue
    if matrix[santa[0]][santa[1]] == 'C':
        matrix[santa[0]][santa[1]] = 'S'
        extra_gifts = 0
        if matrix[santa[0] + 1][santa[1]] != '-' and matrix[santa[0] + 1][santa[1]] != 'C':
            if matrix[santa[0] + 1][santa[1]] == "V":
                nice -= 1
            extra_gifts += 1
            matrix[santa[0] + 1][santa[1]] = '-'
        if matrix[santa[0] - 1][santa[1]] != '-' and matrix[santa[0] - 1][santa[1]] != 'C':
            if matrix[santa[0] - 1][santa[1]] == 'V':
                nice -= 1
            extra_gifts += 1
            matrix[santa[0] - 1][santa[1]] = '-'
        if matrix[santa[0]][santa[1] - 1] != '-' and matrix[santa[0]][santa[1] - 1] != 'C':
            if matrix[santa[0]][santa[1] - 1] == "V":
                nice -= 1
            extra_gifts += 1
            matrix[santa[0]][santa[1] - 1] = '-'
        if matrix[santa[0]][santa[1] + 1] != '-' and matrix[santa[0]][santa[1] + 1] != 'C':
            if matrix[santa[0]][santa[1] + 1] == 'V':
                nice -= 1
            extra_gifts += 1
            matrix[santa[0]][santa[1] + 1] = '-'
        gifts -= extra_gifts
        happy += extra_gifts
        if gifts <= 0:
            break
        happy_position = [santa[0], santa[1]]
    elif matrix[santa[0]][santa[1]] == 'X':
        matrix[santa[0]][santa[1]] = 'S'
        continue
    elif matrix[santa[0]][santa[1]] == 'V':
        matrix[santa[0]][santa[1]] = 'S'
        gifts -= 1
        nice -= 1
        happy += 1
    if gifts == 0:
        no_gifts = True
        break
    elif matrix[santa[0]][santa[1]] == '-':
        continue
wtf = False
if nice > 0:
    wtf = True
    print("Santa ran out of presents!")
for cell in matrix:
    print(' '.join(cell))
if wtf:
    print(f"No presents for {nice} nice kid/s.")
if nice == 0:
    print(f"Good job, Santa! {happy} happy nice kid/s.")