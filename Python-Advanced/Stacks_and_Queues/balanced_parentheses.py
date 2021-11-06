parentheses = input()
is_balanced = True
opening = []
mapper = {'{': '}', '(':')','[':']'}
for p in parentheses:
    if p in "({[":
        opening.append(p)
    else:
        if not opening:
            is_balanced = False
            break
        current_opening_p = opening.pop()
        if mapper[current_opening_p] == p:
            continue
        else:
            is_balanced = False
            break
if is_balanced:
    print('YES')
else:
    print("NO")