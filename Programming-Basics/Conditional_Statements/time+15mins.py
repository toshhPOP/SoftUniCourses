hour = int(input())
minutes = int(input())
minutes += 15
if minutes == 60:
    minutes = 0
    hour += 1
    if hour >= 24:
        hour = 0
    print(f"{hour}:0{minutes}")
elif minutes > 60:
    hour += 1
    if hour >= 24:
        hour = 0
    mins = minutes - 60
    if mins < 10:
        print(f"{hour}:0{mins}")
    else:

        print(f"{hour}:{mins}")
else:
    print(f"{hour}:{minutes}")
