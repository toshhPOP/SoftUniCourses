text = [a for a in input()]
print(''.join(text.pop() for a in range(len(text))))
