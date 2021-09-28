numbers = int(input())
registered_cars = {}
unregistered_cars = {}
for i in range(numbers):
    command = input().split()
    action = command[0]
    user = command[1]
    if action == "unregister":
        if user not in registered_cars:
            print(f"ERROR: user {user} not found")
        else:
            print(f"{user} unregistered successfully")
            registered_cars.pop(user)
    elif action == "register":
        plate_number = command[2]
        if user not in registered_cars:
            registered_cars[user] = plate_number
            print(f"{user} registered {registered_cars[user]} successfully")
        else:
            print(f"ERROR: already registered with plate number {registered_cars[user]}")
for user,car_number in registered_cars.items():
    print(f"{user} => {car_number}")

