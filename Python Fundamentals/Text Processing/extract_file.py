path = input()
index = 0
for i in range(len(path)):
    if path[i] == ".":
        extension = path[i+1:]
        index = i+1
        break
for a in reversed(range(index)):
    if path[a] == "\\":
        file_name = path[a+1:index]
        file_name = "".join([a for a in file_name if a != "."])
        print(f"File name: {file_name}")
        print(f"File extension: {extension}")
        exit()

