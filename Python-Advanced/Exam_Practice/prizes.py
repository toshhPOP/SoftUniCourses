def is_in_range(row, col, n):
    if 0 <= row < n and 0 <= col < n:
        return True
    return False


def score(r, c):
    if is_in_range(r, c, size):
        return r, c
    else:
        return False

def total(cell,points):
    cell = current_cell
    tr, tc = current_cell[0], current_cell[1]
    if matrix[tr][tc] == 'B':
        if current_cell not in buckets:
            buckets.append(current_cell)
            for r in range(size):
                if matrix[r][tc].isdigit():
                    points += int(matrix[r][tc])
    else:
        points = 0
    return points
size = 6
matrix = [[x for x in input().split()] for _ in range(size)]
points = 0
buckets = []
for i in range(3):
    shot = input()
    throw = [int(x) for x in shot[1:-1].split(', ')]
    tr, tc = throw[0], throw[1]
    current_cell = score(tr, tc)
    if current_cell:
        points = total(current_cell,points)
gift = ''
if 100 <= points <= 199:
    gift = 'Football'
elif 200 <= points <= 299:
    gift = 'Teddy Bear'
elif points >= 300:
    gift = 'Lego Construction Set'
if points < 100:
    print(f"Sorry! You need {100 - points} points more to win a prize.")
else:
    print(f"Good job! You scored {points} points, and you've won {gift}.")