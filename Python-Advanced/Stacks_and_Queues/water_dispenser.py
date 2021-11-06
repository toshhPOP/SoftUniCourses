from collections import deque

queue = deque()
quantity = int(input())
while True:
    command = input()
    if not command == "Start":
        queue.append(command)
    else:
        break
while True:
    another = input()
    if another == "End":
        print(f"{quantity} liters left")
        break
    elif another.isdigit():
        if int(another) <= quantity:
            quantity -= int(another)
            print(f"{queue.popleft()} got water")
        else:
            print(f"{queue.popleft()} must wait")
    else:
        another = another.split()
        quantity += int(another[1])
