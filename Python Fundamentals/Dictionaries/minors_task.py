dictionary = {}
while True:
    command = input()
    if command == "stop":
        break
    if command not in dictionary:
        dictionary[command] = 0
    command_1 = int(input())
    dictionary[command] += command_1
for key, value in dictionary.items():
    print(f"{key} -> {value}")
