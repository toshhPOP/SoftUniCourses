import re

command = input()
result = []
while command != "":
    num_pattern = r"\d+"
    digit = re.finditer(num_pattern,command)
    for e in digit:
        result.append(e.group())
    command = input()
result = [a for a in result]
print(' '.join(result))