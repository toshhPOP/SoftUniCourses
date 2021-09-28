text = input()
digits = ''
strings = ''
others = ''
for e in text:
    if e.isdigit():
        digits += e
    elif e.isalpha():
        strings += e
    else:
        others += e
print(f"{digits}\n{strings}\n{others}")
