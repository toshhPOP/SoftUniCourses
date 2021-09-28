explosion = input()
new = ''
power = 0
for i in range(len(explosion)):

    if explosion[i] == ">":
        new += explosion[i]
        power += int(explosion[i+1])
    else:
        if power > 0:
            power -= 1
        else:
            new += explosion[i]
print(new)