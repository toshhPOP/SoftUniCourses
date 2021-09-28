strings = input().split()
result = 0
for word in strings:
    for sym in range(len(word)):
        number = [a for a in word[1:] if a.isnumeric()]
        num = int("".join(number))
        next_sym = "".join([a for a in word[1:] if a.isalpha()])
        if word[sym].isupper():
            letter_position = ord(word[sym]) - 64
            result += num / letter_position
        elif word[sym].islower():
            letter_position = ord(word[sym]) - 96
            result += num * letter_position
        if next_sym.isupper():
            letter_position = ord(next_sym) - 64
            result -= letter_position
        else:
            letter_position = ord(next_sym) - 96
            result += letter_position
        break
print(f"{result:.2f}")