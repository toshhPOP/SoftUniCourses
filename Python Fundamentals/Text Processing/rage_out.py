text = input().upper()
digit = ''
for i in range(len(text)):
    if text[i].isdigit():
        if not i+1 >= len(text)-1:
            if text[i+1].isdigit():
                digit += text[i] + text[i+1] + " "
            else:
                if text[i] not in digit:
                    digit += text[i] + " "
        else:
            digit += text[i]
digit = digit.split()
digit = [int(x) for x in digit]
result = ''
while len(digit) > 0:
    for a in digit:
        word = text[:text.index(str(a))]
        result += word * a
        text = text.replace(word, '', 1)
        text = text.replace(str(a), '', 1)
        digit.remove(a)
        break
unique = set(result)
print(f"Unique symbols used: {len(unique)}\n{result}")