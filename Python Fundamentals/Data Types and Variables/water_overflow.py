number = int(input())
tank_v = 255
for i in range(1, number + 1):
    litters = int(input())
    tank_v -= litters
    if tank_v < 0:
        print("Insufficient capacity!")
        tank_v += litters
new_v = 255 - tank_v
print(new_v)
