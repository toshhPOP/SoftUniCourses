from collections import deque
price = int(input())
barrel_size = int(input())
bullets = deque(int(x) for x in input().split())
locks = deque(int(x) for x in input().split())
value = int(input())
shots = 0
fired = 0
while bullets:
    if locks:
        power = bullets.pop()
        lock = locks.popleft()
        shots += 1
        fired += 1
        if power <= lock:
            print("Bang!")
        else:
            print("Ping!")
            locks.appendleft(lock)
        if shots == barrel_size:
            shots = 0
            if bullets:
                print("Reloading!")
    else:
        break
if locks:
    print(f"Couldn't get through. Locks left: {len(locks)}")
else:
    print(f"{len(bullets)} bullets left. Earned ${value -(price*fired)}")