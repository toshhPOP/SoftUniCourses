cards = input().split(" ")
A = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
B = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
for card in cards:
    team, number = card.split("-")
    if team == "A":
        if int(number) not in A:
            continue
        A.remove(int(number))
    elif team == "B":
        if int(number) not in B:
            continue
        B.remove(int(number))
print(f"Team A - {len(A)}; Team B - {len(B)}")
if len(A) < 7 or len(B) < 7:
    print("Game was terminated")

