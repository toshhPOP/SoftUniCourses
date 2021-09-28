number = int(input())
cars = {}
for i in range(number):
    command = input().split("|")
    model = command[0]
    if model not in cars:
        cars[model] = []
    mile = int(command[1])
    fuel = int(command[2])
    cars[model].append(mile)
    cars[model].append(fuel)
while True:
    action = input()
    if action == "Stop":
        cars = sorted(cars.items(), key=lambda x: (-x[1][0], x[0]))
        for car, mileage in cars:
            print(f"{car} -> Mileage: {mileage[0]} kms, Fuel in the tank: {mileage[1]} lt.")
        break
    action = action.split(" : ")
    if action[0] == "Drive":
        digits = cars.get(action[1])
        if digits[1] < int(action[3]):
            print("Not enough fuel to make that ride")
        else:
            print(f"{action[1]} driven for {action[2]} kilometers. {action[3]} liters of fuel consumed.")
            digits[0] += int(action[2])
            if digits[0] >= 100000:
                print(f"Time to sell the {action[1]}!")
                cars.pop(action[1])
            digits[1] -= int(action[3])
    elif action[0] == "Refuel":
        digits = cars.get(action[1])
        digits[1] += int(action[2])
        if digits[1] > 75:
            digits[1] -= int(action[2])
            print(f"{action[1]} refueled with {75 - digits[1]} liters")
            digits[1] = 75
            continue
        print(f"{action[1]} refueled with {int(action[2])} liters")
    elif action[0] == "Revert":
        digits = cars.get(action[1])
        digits[0] -= int(action[2])
        if digits[0] < 10000:
            digits[0] = 10000
            continue
        print(f"{action[1]} mileage decreased by {int(action[2])} kilometers")
