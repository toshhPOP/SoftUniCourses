import re

variable_pattern = r"(\b_[A-Za-z0-9]+\b)"

command = input()
variable = re.finditer(variable_pattern,command)
result = []
for e in variable:
    result.append(e.group().strip("_"))
print(','.join(result))
