numbers = [float(x) for x in input().split()]
new = []
for a in numbers:
    if a not in new:
        new.append(a)
for i in new:
    print(f"{i} - {numbers.count(i)} times")
