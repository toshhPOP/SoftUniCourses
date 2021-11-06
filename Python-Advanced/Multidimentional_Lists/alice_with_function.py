def is_valid_position(matrix, r, c):
    wonderland = len(matrix)
    if r < 0 or c < 0 or r >= size or c >= size:
        return False
    return True


def next_position(command, r, c):
    if command == 'up':
        if is_valid_position(matrix, alice_position[0] - 1, alice_position[1]):
            alice_position[0] -= 1
            result = alice_position[0], alice_position[1]
            return result
        else:
            return False
    if command == 'left':
        if is_valid_position(matrix, alice_position[0], alice_position[1] - 1):
            alice_position[1] -= 1
            result = alice_position[0], alice_position[1]
            return result
        else:
            return False
    if command == 'down':
        if is_valid_position(matrix, r + 1, c):
            alice_position[0] += 1
            result = alice_position[0], alice_position[1]
            return result
        else:
            return False
    if command == 'right':
        if is_valid_position(matrix, r, c + 1):
            alice_position[1] += 1
            result = alice_position[0], alice_position[1]
            return result
        else:
            return False


path = {'Alice': []}
collected = False
party = True
size = int(input())
matrix = [[a for a in input().split()] for i in range(size)]
for r in range(size):
    for c in range(size):
        if matrix[r][c] == "A":
            alice_position = [r, c]
tea_bags = 0
matrix[alice_position[0]][alice_position[1]] = '*'
while True:
    command = input()
    result = next_position(command, alice_position[0], alice_position[1])
    if result:
        path['Alice'].append([result[0], result[1]])
        if matrix[result[0]][result[1]].isdigit():
            tea_bags += int(matrix[result[0]][result[1]])
            if tea_bags >= 10:
                collected = True
                break
        if matrix[result[0]][result[1]] == 'R':
            party = False
            break
    else:
        party = False
        break
for step in path.values():
    for el in step:
        matrix[el[0]][el[1]] = '*'
if not party:
    print("Alice didn't make it to the tea party.")
if collected:
    print("She did it! She went to the party.")
for i in matrix:
    print(' '.join(i))
