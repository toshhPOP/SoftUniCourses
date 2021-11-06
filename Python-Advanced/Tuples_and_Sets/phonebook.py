dd = {}
while True:
    command = input()
    if len(command) > 1:
        name, number = command.split('-')
        if number not in dd:
            dd[name] = number
        else:
            dd[name] = number
    else:
        break
n = int(command)
for i in range(n):
    name = input()
    if name in dd:
        print(f"{name} -> {dd[name]}")
    else:
        print(f"Contact {name} does not exist")
