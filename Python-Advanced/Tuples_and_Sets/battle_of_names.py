num = int(input())
odd = set()
even = set()
for i in range(1, num + 1):
    name = input()
    total = sum([ord(a) for a in name]) // i
    if total % 2 == 0:
        even.add(total)
    else:
        odd.add(total)
result = set()
if sum(even) == sum(odd):
    result = odd.union(even)
elif sum(odd) > sum(even):
    result = odd.difference(even)
elif sum(even) > sum(odd):
    result = odd.symmetric_difference(even)
print(', '.join(str(a) for a in result))
