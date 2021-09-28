num = int(input())
age = 0
name = ''
for i in range(num):
    text = input()
    for i in range(len(text)):
        if ord(text[i]) == 64:
            name = text[i+1:]
            for e in range(len(name)):
                if ord(name[e]) == 124:
                    name = name[:int(e)]
                    break
    for i in range(len(text)):
        if ord(text[i]) == 35:
            age = text[i+1:]
            for e in range(len(age)):
                if ord(age[e]) == 42:
                    age = age[:int(e)]
                    break
    print(f"{name} is {age} years old.")
