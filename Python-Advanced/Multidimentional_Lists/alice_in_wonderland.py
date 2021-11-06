def is_valid_position(matrix, r, c):
    size = len(matrix)
    if r < 0 or c < 0 or r >= size or c >= size:
        return False
    return True
path = []
party = True
collected = False
tea_bags = 0
size = int(input())
matrix = [[x for x in input().split()] for i in range(size)]
for r in range(size):
    for c in range(size):
        if matrix[r][c] == "A":
            alice_position = [r, c]
path.append(alice_position)
command = input()
while command != '':
    if command == 'down':
        if is_valid_position(matrix, alice_position[0] + 1, alice_position[1]):
            alice_position = [alice_position[0] + 1, alice_position[1]]
            result = matrix[alice_position[0]][alice_position[1]]
            result = matrix[alice_position[0]][alice_position[1]]
            path.append(alice_position)
            if result.isdigit():
                tea_bags += int(result)
                if tea_bags >= 10:
                    collected = True
                    break
            if result == 'R':
                party = False
                break
        else:
            party = False
            break
    elif command == 'up':
        if is_valid_position(matrix, alice_position[0] - 1, alice_position[1]):
            alice_position = [alice_position[0] - 1, alice_position[1]]
            result = matrix[alice_position[0]][alice_position[1]]
            path.append(alice_position)
            if result.isdigit():
                tea_bags += int(result)
                if tea_bags >= 10:
                    collected = True
                    break
            if result == 'R':
                party = False
                break
        else:
            party = False
            break
    elif command == 'left':
        if is_valid_position(matrix, alice_position[0], alice_position[1]-1):
            alice_position = [alice_position[0], alice_position[1]-1]
            result = matrix[alice_position[0]][alice_position[1]]
            path.append(alice_position)
            if result.isdigit():
                tea_bags += int(result)
                if tea_bags >= 10:
                    collected = True
                    break
            if result == 'R':
                party = False
                break
        else:
            party = False
            break
    elif command == 'right':
        if is_valid_position(matrix, alice_position[0], alice_position[1]+1):
            alice_position = [alice_position[0], alice_position[1]+1]
            result = matrix[alice_position[0]][alice_position[1]]
            path.append(alice_position)
            if result.isdigit():
                tea_bags += int(result)
                if tea_bags >= 10:
                    collected = True
                    break
            if result == 'R':
                party = False
                break
        else:
            party = False
            break
    command = input()
for el in path:
    matrix[el[0]][el[1]] = '*'
if not party:
    print("Alice didn't make it to the tea party.")
elif collected:
    print("She did it! She went to the party.")
for el in range(len(matrix)):
    print(' '.join(matrix[el]))