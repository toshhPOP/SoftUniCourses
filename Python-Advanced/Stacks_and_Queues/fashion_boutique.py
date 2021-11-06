clothes = [int(x) for x in input().split()]
rack_capacity = int(input())
counter = 1
total = 0
while clothes:
    pieces = clothes.pop()
    total += pieces
    if total == rack_capacity:
        if clothes:
            counter += 1
        total = 0
    elif total > rack_capacity:
        counter += 1
        clothes.append(pieces)
        total = 0
print(counter)