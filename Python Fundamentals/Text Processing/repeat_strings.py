text = input().split()
result = ''
for word in text:
    print(word * len(word), end='')
