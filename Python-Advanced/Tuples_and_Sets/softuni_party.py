n = int(input())
reservations = {input()for _ in range(n)}
while True:
    command = input()
    if command == "END":
        break
    reservations.remove(command)
print(len(reservations))
def is_vip(reservations):
    return reservations[0].isdigit()

vip = sorted(g for g in reservations if is_vip(g))
regular = sorted(g for g in reservations if not is_vip(g))
[print(g) for g in vip]
[print(g) for g in regular]