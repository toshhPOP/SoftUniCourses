text = input()
for i in sorted(set(text)):
    print(f"{i}: {text.count(i)} time/s")