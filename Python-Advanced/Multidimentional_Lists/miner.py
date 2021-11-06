def read_matrix():
    rows = 7
    matrix = [[x for x in input().split()] for i in range(rows)]
    return matrix


first_player, second_player = input().split(', ')
players = {
    first_player: {'score': 501, 'shots': 0},
    second_player: {'score': 501, 'shots': 0}
}
matrix = read_matrix()
rows = len(matrix)
cols = len(matrix[rows - 1])
bullseye = False
turn = 0
while not bullseye:
    coordinates = input()
    x = int(coordinates[1])
    y = int(coordinates[4])
    if turn % 2 == 0:
        player = first_player
    else:
        player = second_player
    if x not in range(rows) or y not in range(cols):
        players[player]['shots'] += 1
        turn += 1
        continue
    players[player]['shots'] += 1
    sector = matrix[x][y]
    if sector.isdigit():
        players[player]["score"] -= int(sector)
    else:
        if matrix[x][y] == "B":
            bullseye = True
            break
        elif matrix[x][y] == 'D':
            points = (int(matrix[x - x][y]) + int(matrix[rows - 1][y]) + int(matrix[x][y - y]) + int(
                matrix[x][cols - 1])) * 2
        elif matrix[x][y] == 'T':
            points = (int(matrix[x - x][y]) + int(matrix[rows - 1][y]) + int(matrix[x][y - y]) + int(
                matrix[x][cols - 1])) * 3
        players[player]['score'] -= points
        if players[player]['score'] <= 0:
            break
    turn += 1
if bullseye:
    print(f"{player} won the game with {players[player]['shots']} throws!")
else:
    print(f"{player} won the game with {players[player]['shots']} throws!")