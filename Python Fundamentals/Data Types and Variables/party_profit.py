companions = int(input())
days = int(input())
companions_coins = 0
coins = 0
for i in range(1, days + 1):
    coins += 50
    if i % 10 == 0:
        companions -= 2
    if i % 15 == 0:
        companions += 5
    if i % 3 == 0:
        coins -= companions * 3
    if i % 5 == 0 and i % 3 == 0:
        coins += 20 * companions
        coins -= companions * 2
    elif i % 5 == 0:
        coins += 20 * companions
    coins -= companions * 2
print(f"{companions} companions received {int(coins / companions)} coins each.")
