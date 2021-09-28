import re

furniture_validator = r"(?P<sep>[>>]+)(?P<furniture>[A-Za-z]+)(?P<del><<)(?P<price>[0-9(.)*]+)!(?P<qnt>\d+)"
result = []
total = 0
while True:
    command = input()
    if command == "Purchase":
        print(f"Bought furniture:")
        for a in result:
            print(a)
        print(f"Total money spend: {total:.2f}")
        exit()
    furniture = re.finditer(furniture_validator, command)
    for el in furniture:
        total += float(el.group("price")) * float(el.group("qnt"))
        result.append(el.group("furniture"))
        break