text = input()
emoji = ''
for a in range(len(text)):
    if text[a] == ":":
        print(f"{text[a]}{text[a+1]}")