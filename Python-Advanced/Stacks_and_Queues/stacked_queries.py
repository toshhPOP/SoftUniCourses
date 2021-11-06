num = int(input())
stack = []
for i in range(num):
    command = input()
    if '1' in command:
        stack.append(int(command.split()[1]))
    elif command == "2":
        if stack:
            stack.pop()
    elif command == '3':
        if stack:
            print(max(stack))
    elif command[0] == '4':
        if stack:
            print(min(stack))
print(', '.join(str(stack.pop()) for a in range(len(stack)) if len(stack) > 0))