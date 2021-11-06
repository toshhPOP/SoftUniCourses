num = int(input())
unique = set(input() for a in range(num))
print('\n'.join([a for a in unique]))
