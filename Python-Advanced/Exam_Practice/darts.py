def valid_shot(row, col, n):
    if 0 <= row < n and 0 <= col < n:
        return True
    return False


def player_turn(c):
    if c % 2 != 0:
        name = first
    else:
        name = second

    return name


def play(total):
    if total.isdigit():
        players[player]['score'] -= int(score)
    elif total == 'D':
        points = (int(darts[x][0]) + int(darts[x][size - 1]) + int(darts[0][y]) + int(darts[size - 1][y])) * 2
        players[player]['score'] -= points
    elif total == 'T':
        points = (int(darts[x][0]) + int(darts[x][size - 1]) + int(darts[0][y]) + int(darts[size - 1][y])) * 3
        players[player]['score'] -= points
    elif total == 'B':
        players[player]['score'] = 501
    return players


def check_win(players):
    if players[player]['score'] == 501:
        print(f"{player} won the game with {players[player]['shots']} throws!")
        return True
    elif players[player]['score'] <= 0:
        print(f"{player} won the game with {players[player]['shots']} throws!")
        return True
    return False


def throws(r, c):
    players[player]['shots'] += 1
    if valid_shot(r, c, size):
        return darts[r][c]
    return False


counter = 0
first, second = input().split(', ')
size = 7
darts = [[x for x in input().split()] for _ in range(size)]
players = {
    first: {'score': 501, 'shots': 0},
    second: {'score': 501, 'shots': 0}
}

while True:
    shot = input()
    shot = [int(x) for x in shot[1:-1].split(', ')]
    counter += 1
    x, y = shot[0], shot[1]
    player = player_turn(counter)
    score = throws(x, y)
    if score:
        players = play(score)
        if check_win(players):
            break
