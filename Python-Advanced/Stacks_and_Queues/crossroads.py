from collections import deque

green_duration = int(input())
free_window = int(input())
cars = deque()
safe = 0
duration = green_duration
command = input()
while command != "END":
    if not command == "green":
        duration = green_duration
        cars.append(command)
    else:
        for i in range(len(cars)):
            car = cars.popleft()
            vehicle = car
            car = deque(a for a in car)
            if duration == 0:
                if free_window < len(car):
                    continue
            for i in range(duration):
                if len(car) > 0:
                    car.popleft()
                    duration -= 1
                else:
                    break
            if duration > 0:
                safe += 1
            else:
                for i in range(free_window):
                    if len(car) > 0:
                        car.popleft()
                        free_window -= 1
                    else:
                        break
                if free_window > len(car):
                    safe += 1
                else:
                    print(f"A crash happened!\n"
                          f"{vehicle} was hit at {car.popleft()}.")
                    exit()
    command = input()
print(f"Everyone is safe.\n"f"{safe} total cars passed the crossroads.")
