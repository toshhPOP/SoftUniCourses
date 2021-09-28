import re

name_pattern = r"(?P<name>[A-Za-z])"
distance_pattern = r"(?P<distance>\d)"
my_dict = {}
names = input().split(", ")

while True:
    command = input()
    if command == 'end of race':
        break
    player = re.findall(name_pattern, command)

    points = [int(x) for x in re.findall(distance_pattern, command)]
    sum(points)
    if not "".join(player) in names:
        continue
    if not ''.join(player) in my_dict:
        my_dict[''.join(player)] = sum(points)
    else:
        my_dict[''.join(player)] += sum(points)
my_dict = sorted(my_dict.items(),key=lambda x: -x[1])
top = [a for a in my_dict[::]]
print(f"1st place: {top[0][0]}\n2nd place: {top[1][0]}\n3rd place: {top[2][0]}")