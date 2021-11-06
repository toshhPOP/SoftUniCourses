from collections import deque

males = [int(x) for x in input().split()]
females = deque(int(x) for x in input().split())
matches = 0
while males and females:
    man = males[-1]
    woman = females[0]
    if man <= 0:
        males.pop()
        continue
    elif woman <= 0:
        females.popleft()
        continue
    if man % 25 == 0:
        males = males[:-3]
        continue
    if woman % 25 == 0:
        for _ in range(2):
            females.popleft()
        continue

    if man == woman:
        matches += 1
        males.pop()
        females.popleft()
    else:
        males[-1] -= 2
        if males[-1] <= 0:
            males.pop()
        females.popleft()
print(f"Matches: {matches}")
if males:
    print(f"Males left: {', '.join(str(a) for a in males[::-1])}")
else:
    print(f"Males left: none")
if females:
    print(f"Females left: {', '.join(str(a) for a in females)}")
else:
    print('Females left: none')
