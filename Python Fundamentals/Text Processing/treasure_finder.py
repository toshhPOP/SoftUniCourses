key = [int(x) for x in input().split()]
counter = 0
while True:
    command = input()
    if command == "find":
        break
    command = [a for a in command]
    for el in range(len(command)):
        if counter < len(key):
            new = chr(ord(command[el]) - key[counter])
            command[el] = new
            counter += 1
        else:
            counter = 0
            new = chr(ord(command[el]) - key[counter])
            command[el] = new
            counter += 1
    index = command.index("&")
    treasure = command[index + 1:]
    treasure = "".join(treasure[:treasure.index("&")])
    index_1 = command.index("<")
    coordinates = command[index_1 + 1:]
    coordinates = "".join(coordinates[:coordinates.index(">")])
    counter = 0
    print(f"Found {treasure} at {coordinates}")