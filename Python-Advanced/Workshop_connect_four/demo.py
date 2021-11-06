import sys
from io import StringIO

test_input = '''
1
2
3
2
1
'''
sys.stdin = StringIO(test_input)


def get_player_choice(player):
    choice = input(f"Player {player}, please choose a columne")
    return choice


def apply_player_choice():
    pass


def check_win_condition():
    pass


def play(board):
    current_player, other_player = 1, 2
    while True:
        player_choice = get_player_choice(current_player)
        # apply_player_choice()
        # check_win_condition()
        print(get_player_choice(current_player))


def create_board(rows_count, columns_count):
    return [[None] * columns_count for _ in range(rows_count)]


def print_board(board):
    for row in board:
        print(row)


board = create_board(6, 7)
print_board(board)
